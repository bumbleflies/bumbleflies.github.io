import json
from os import path
from bs4 import BeautifulSoup
import pytest as pytest

from _tests.helper import query_site

@pytest.fixture()
def redirects(path_to_site):
    with open(path.join(path_to_site, 'redirects.json')) as redirect_file:
        return json.load(redirect_file)

class TestRedirects:
    # https://www.google.com/search?q=+site%3Abumbleflies.de
    @pytest.mark.parametrize('page',
                         ['imprint', 'privacy', 'stayintheloop', 'obs', 'os-check', 'os-principles'])
    def test_page_is_redirecting(self, bumbleserve, page, redirects):

        assert redirects[f'/{page}']

        assert query_site(bumbleserve, page).find(name='title').text == 'Redirecting...'
