import os
import shutil
import subprocess
import time
import unittest
from pathlib import Path
from urllib.parse import urljoin

import requests
import pytest

from pytest_nginx import factories
from bs4 import BeautifulSoup
from more_itertools import one


@pytest.fixture(scope='session')
def nginx_server_root():
    path = Path('_test_site')
    path.mkdir(exist_ok=True)
    assert shutil.which('nginx')=='/usr/sbin/nginx'
    return path.absolute()


nginx_proc = factories.nginx_proc("nginx_server_root")


@pytest.fixture(scope='session')
def bumbleweb(nginx_proc):
    result = subprocess.run(['bundle', 'exec', 'jekyll', 'build', '-d', nginx_proc.server_root], cwd='..',
                            capture_output=True, text=True)
    assert 'done in' in result.stdout
    yield nginx_proc
    # ugly teardown to prevent error that nginx was terminted with code = 15
    subprocess.run(['killall', 'nginx'])
    time.sleep(1)


def query_site(bumbleweb, path=''):
    response = requests.get(urljoin(f'http://{bumbleweb.host}:{bumbleweb.port}', path))
    if response.status_code == 404 and not path.endswith('.html'):
        response = requests.get(urljoin(f'http://{bumbleweb.host}:{bumbleweb.port}', f'{path}.html'))

    assert response.status_code == 200, response
    return BeautifulSoup(response.content, features='html.parser')


def assert_stylesheet_present(stylesheet_name, stylesheets):
    found_stylesheet = one(filter(lambda s: stylesheet_name in s.attrs['href'], stylesheets))
    assert Path('_test_site', found_stylesheet.attrs['href']).exists()


def assert_link_present(link_name, link_target, links, bumbleweb):
    found_link = one(filter(lambda s: link_target in s.attrs['href'], links))
    assert found_link.text == link_name
    query_site(bumbleweb, path=found_link.attrs['href'])


def test_title(bumbleweb):
    assert 'bumbleflies | 🦋' in query_site(bumbleweb).find(name='title').text


def test_stylesheets_for_theme_present(bumbleweb):
    stylesheets = query_site(bumbleweb).find_all(rel='stylesheet')
    assert_stylesheet_present('bootstrap.min.css', stylesheets)
    assert_stylesheet_present('all.min.css', stylesheets)
    assert_stylesheet_present('agency.css', stylesheets)
    assert_stylesheet_present('custom.css', stylesheets)


def test_navigation(bumbleweb):
    nav_links = query_site(bumbleweb).find_all('a', {'class': 'nav-link'})
    assert_link_present('Leistungen', '#Leistungen', nav_links, bumbleweb)
    assert_link_present('Über uns', '#about', nav_links, bumbleweb)
    assert_link_present('Team', '#Team', nav_links, bumbleweb)
    assert_link_present('open:bumble:space', 'obs', nav_links, bumbleweb)

def test_legal(bumbleweb):
    legal_links = query_site(bumbleweb).find('ul', {'class': 'quicklinks'}).findChildren('a')
    assert len(legal_links)==2
    assert_link_present('Impressum', 'imprint', legal_links, bumbleweb)
    assert_link_present('Datenschutzerklärung', 'privacy', legal_links, bumbleweb)
