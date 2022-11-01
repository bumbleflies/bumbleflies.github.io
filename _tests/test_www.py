import subprocess
import time
from http.client import HTTPConnection
from pathlib import Path
from urllib.parse import urljoin

import pytest
import requests
from bs4 import BeautifulSoup
from more_itertools import one


def http_server_process(directory: str) -> subprocess.Popen:
    """
    Call python's http.server module as a child process, wait for initialization and yield server for tests.
    """

    server = subprocess.Popen(['python', '-m', 'http.server', '--directory', directory],
                              encoding='utf-8',
                              universal_newlines=True)

    retries = 5
    while retries > 0:
        conn = HTTPConnection('localhost:8000')
        try:
            conn.request('HEAD', '/')
            response = conn.getresponse()
            if response is not None:
                return server
        except ConnectionRefusedError:
            time.sleep(0.5)
            retries -= 1

    raise RuntimeError('Failed to start http server')


@pytest.fixture(scope='session')
def path_to_site():
    return Path('_test_site').absolute()


@pytest.fixture(scope='session')
def bumblebuild(path_to_site: Path):
    result = subprocess.run(['bundle', 'exec', 'jekyll', 'build', '-d', path_to_site], cwd='..',
                            capture_output=True, text=True)
    assert 'done in' in result.stdout


@pytest.fixture(scope='session')
def bumbleserve(path_to_site, bumblebuild):
    class Server:
        def __init__(self):
            self.host = 'localhost'
            self.port = 8000

    server_process = http_server_process(path_to_site)
    yield Server()

    server_process.terminate()
    server_process.wait()


def query_site(bumbleserve, path=''):
    response = requests.get(urljoin(f'http://{bumbleserve.host}:{bumbleserve.port}', path))
    if response.status_code == 404 and not path.endswith('.html'):
        response = requests.get(urljoin(f'http://{bumbleserve.host}:{bumbleserve.port}', f'{path}.html'))

    assert response.status_code == 200, response
    return BeautifulSoup(response.content, features='html.parser')


def assert_stylesheet_present(stylesheet_name, stylesheets):
    found_stylesheet = one(filter(lambda s: stylesheet_name in s.attrs['href'], stylesheets))
    assert Path('_test_site', found_stylesheet.attrs['href']).exists()


def assert_link_present(link_name, link_target, links, bumbleserve):
    found_link = one(filter(lambda s: link_target in s.attrs['href'], links))
    assert found_link.text == link_name
    query_site(bumbleserve, path=found_link.attrs['href'])


def test_title(bumbleserve):
    assert 'bumbleflies | 🦋' in query_site(bumbleserve).find(name='title').text


def test_stylesheets_for_theme_present(bumbleserve):
    stylesheets = query_site(bumbleserve).find_all(rel='stylesheet')
    assert_stylesheet_present('bootstrap.min.css', stylesheets)
    assert_stylesheet_present('all.min.css', stylesheets)
    assert_stylesheet_present('agency.css', stylesheets)
    assert_stylesheet_present('custom.css', stylesheets)


def test_navigation(bumbleserve):
    nav_links = query_site(bumbleserve).find_all('a', {'class': 'nav-link'})
    assert_link_present('Leistungen', '#Leistungen', nav_links, bumbleserve)
    assert_link_present('Über uns', '#about', nav_links, bumbleserve)
    assert_link_present('Team', '#Team', nav_links, bumbleserve)
    assert_link_present('open:bumble:space', 'obs', nav_links, bumbleserve)


def test_legal(bumbleserve):
    legal_links = query_site(bumbleserve).find('ul', {'class': 'quicklinks'}).findChildren('a')
    assert_link_present('Impressum', 'imprint', legal_links, bumbleserve)
    assert_link_present('Datenschutzerklärung', 'privacy', legal_links, bumbleserve)
