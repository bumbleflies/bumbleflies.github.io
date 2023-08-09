from os import path
from typing import TextIO
from urllib.parse import urlparse

import pytest as pytest
from bs4 import BeautifulSoup

from _tests.helper import query_site, assert_stylesheet_present


def load_locs(sitemap: TextIO):
    bs_map = BeautifulSoup(sitemap, 'lxml')
    return filter(lambda l: '/assets' not in l, map(lambda loc: urlparse(loc.text).path,
                                                    bs_map.find_all('loc')))


@pytest.fixture(scope='session')
def all_pages(path_to_site):
    with open(path.join(path_to_site, 'sitemap.xml')) as sitemap:
        return load_locs(sitemap)


@pytest.fixture(scope='session')
def all_en_pages(path_to_site):
    with open(path.join(path_to_site, 'en', 'sitemap.xml')) as sitemap:
        return load_locs(sitemap)


@pytest.mark.parametrize('stylesheet',
                         ['bootstrap.min.css', 'all.min.css', 'bumble.css', 'custom.css', 'font-faces.css',
                          'flag-icons.min.css'])
class TestWithSitemap:

    def test_stylesheets_for_page_present(self, bumbleserve, all_pages, stylesheet):
        for page in all_pages:
            print(page)
            print(page.startswith('/assets'))
            stylesheets = query_site(bumbleserve, page).find_all(rel='stylesheet')
            assert_stylesheet_present(stylesheet, stylesheets)

    def test_stylesheets_for_en_page_present(self, bumbleserve, all_en_pages, stylesheet):
        for page in all_en_pages:
            print(page)
            stylesheets = query_site(bumbleserve, page).find_all(rel='stylesheet')
            assert_stylesheet_present(stylesheet, stylesheets)
