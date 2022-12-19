import pytest as pytest

from _tests.helper import query_site


# https://www.google.com/search?q=+site%3Abumbleflies.de
@pytest.mark.parametrize('page',
                         ['datenschutz', 'impressum', 'participate', 'online-treffen',
                          'open-space-checkliste', 'open-space-prinzipien-uebersicht'])
def test_page_is_redirecting(bumbleserve, page):
    assert query_site(bumbleserve, page).find(name='title').text == 'Redirecting…'
