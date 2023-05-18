import pytest as pytest

from _tests.helper import query_site, assert_stylesheet_present, assert_link_present


def test_title(bumbleserve):
    assert 'bumbleflies | 🦋' in query_site(bumbleserve).find(name='title').text


@pytest.mark.parametrize('stylesheet',
                         ['bootstrap.min.css', 'all.min.css', 'bumble.css', 'custom.css', 'font-faces.css'])
def test_stylesheets_for_theme_present(bumbleserve, stylesheet):
    stylesheets = query_site(bumbleserve).find_all(rel='stylesheet')
    assert_stylesheet_present(stylesheet, stylesheets)


def test_no_external_stylesheet(bumbleserve):
    stylesheets = query_site(bumbleserve).find_all(rel='stylesheet')
    external_stylesheet = list(filter(lambda s: s.attrs['href'].startswith('http'), stylesheets))
    assert len(external_stylesheet) == 0, f'External Stylesheets not allowed: {external_stylesheet}'


@pytest.mark.parametrize('display, url', [('Leistungen', '#services'),
                                          ('Über uns', '#about'),
                                          ('Team', '#Team'),
                                          ('open:bumble:space', 'obs')])
def test_navigation(bumbleserve, display, url):
    nav_links = query_site(bumbleserve).find_all('a', {'class': 'nav-link'})
    assert_link_present(display, url, nav_links, bumbleserve)


@pytest.mark.parametrize('display, url', [('Impressum', 'imprint'),
                                          ('Datenschutzerklärung', 'privacy')])
def test_legal(bumbleserve, display, url):
    legal_links = query_site(bumbleserve).find('ul', {'class': 'quicklinks'}).findChildren('a')
    assert_link_present(display, url, legal_links, bumbleserve)
