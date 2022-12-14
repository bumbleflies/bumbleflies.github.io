import pytest as pytest

from _tests.helper import query_site, assert_stylesheet_present, assert_link_present

# https://www.google.com/search?q=+site%3Abumbleflies.de
@pytest.mark.parametrize('page',
                         ['datenschutz', 'impressum', 'stayintheloop', 'participate', 'online-treffen'])
def test_page_is_redirecting(bumbleserve, page):
    assert query_site(bumbleserve, page).find(name='title').text == 'Redirecting…'

