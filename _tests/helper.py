from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from more_itertools import one


def query_site(bumbleserve, path=''):
    response = requests.get(urljoin(f'http://{bumbleserve.host}:{bumbleserve.port}', path))
    if response.status_code == 404 and not path.endswith('.html'):
        response = requests.get(urljoin(f'http://{bumbleserve.host}:{bumbleserve.port}', f'{path}.html'))

    assert response.status_code == 200, response
    return BeautifulSoup(response.content, features='html.parser')


def assert_stylesheet_present(stylesheet_name, stylesheets):
    found_stylesheet = one(filter(lambda s: stylesheet_name in s.attrs['href'], stylesheets))
    assert Path(Path(__file__).parent.parent.joinpath('_test_site'), found_stylesheet.attrs['href'].lstrip('/')).exists()


def assert_link_present(link_name, link_target, links, bumbleserve):
    found_link = one(filter(lambda s: link_name in s.text, links))
    assert link_target == found_link.attrs['href']
    query_site(bumbleserve, path=found_link.attrs['href'])
