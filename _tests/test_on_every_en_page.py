import pytest as pytest

from _tests.helper import query_site, assert_link_present, assert_stylesheet_present


@pytest.mark.parametrize('title, page, allowed_stylesheets', [
    ('bumble:retreat', '/en/bumble-retreat', ()),
    ('open:bumble:space', '/en/open-bumble-space', ('https://events.bumbleflies.de/obs-6/widget/v1.css',)),
    ('Imprint', '/en/imprint', ()),
    ('Privacy', '/en/privacy', ()),
    ('Checklist', '/en/open-space-checklist', ()),
    ('Principles', '/en/open-space-principles', ()),
    ('Stay in the loop', '/en/stayintheloop', ()),
])
class TestOnEveryPage:

    def test_allowed_external_stylesheet(self, bumbleserve, title, page, allowed_stylesheets):
        stylesheets = query_site(bumbleserve, page).find_all(rel='stylesheet')
        external_stylesheets = list(filter(lambda s: s.attrs['href'].startswith('http'), stylesheets))

        not_allowed = list(filter(lambda s: s.attrs['href'] not in allowed_stylesheets, external_stylesheets))
        assert len(not_allowed) == 0, f'External Stylesheets not allowed: {not_allowed}'

    def test_title(self, bumbleserve, title, page, allowed_stylesheets):
        assert f'{title} | bumbleflies | 🦋' in query_site(bumbleserve, page).find(name='title').text

    @pytest.mark.parametrize('display, url', [('bumble:retreat', '/en/bumble-retreat'),
                                              # Events
                                              ('Overview', 'https://events.bumbleflies.de/'),
                                              ('open:bumble:space', '/en/open-bumble-space'),
                                              ('open:chat', '/en/openchat'),
                                              # Open Space
                                              ('Principles', '/en/open-space-principles'),
                                              ('Checklist', '/en/open-space-checklist'),
                                              ('About us', '/en/about'),
                                              ])
    def test_navigation(self, bumbleserve, title, page, allowed_stylesheets, display, url):
        nav_links = query_site(bumbleserve, page).find_all('a', {'class': 'nav-link'})
        assert_link_present(display, url, nav_links, bumbleserve)

    @pytest.mark.parametrize('display, url', [('Imprint', '/en/imprint'),
                                              ('Privacy', '/en/privacy')])
    def test_legal(self, bumbleserve, title, page, allowed_stylesheets, display, url):
        legal_links = query_site(bumbleserve, page).find('ul', {'class': 'quicklinks'}).findChildren('a')
        assert_link_present(display, url, legal_links, bumbleserve)
