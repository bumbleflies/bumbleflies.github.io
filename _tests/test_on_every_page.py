import pytest as pytest

from _tests.helper import query_site, assert_link_present, assert_stylesheet_present


@pytest.mark.parametrize('title, page, allowed_stylesheets', [
    ('Startseite', '/', ()),
    ('open:bumble:space', '/open-bumble-space', ('https://events.bumbleflies.de/obs-3/widget/v1.css',)),
    ('Impressum', '/impressum', ()),
    ('Datenschutz', '/datenschutz', ()),
    ('Checkliste', '/open-space-checkliste', ()),
    ('Prinzipien', '/open-space-prinzipien-uebersicht', ()),
    ('Informiert bleiben', '/informiert-bleiben', ()),
])
class TestOnEveryPage:

    @pytest.mark.parametrize('stylesheet',
                             ['bootstrap.min.css', 'all.min.css', 'bumble.css', 'custom.css', 'font-faces.css',
                              'flag-icons.min.css'])
    def test_stylesheets_for_theme_present(self, bumbleserve, title, page, allowed_stylesheets, stylesheet):
        stylesheets = query_site(bumbleserve, page).find_all(rel='stylesheet')
        assert_stylesheet_present(stylesheet, stylesheets)

    def test_allowed_external_stylesheet(self, bumbleserve, title, page, allowed_stylesheets):
        stylesheets = query_site(bumbleserve, page).find_all(rel='stylesheet')
        external_stylesheets = list(filter(lambda s: s.attrs['href'].startswith('http'), stylesheets))

        not_allowed = list(filter(lambda s: s.attrs['href'] not in allowed_stylesheets, external_stylesheets))
        assert len(not_allowed) == 0, f'External Stylesheets not allowed: {not_allowed}'

    def test_title(self, bumbleserve, title, page, allowed_stylesheets):
        assert f'{title} | bumbleflies | 🦋' in query_site(bumbleserve, page).find(name='title').text

    @pytest.mark.parametrize('display, url', [('Home', '/'),
                                              # Events
                                              ('Übersicht', 'https://events.bumbleflies.de/'),
                                              ('open:bumble:space', '/open-bumble-space'),
                                              ('open:chat', 'https://openchat.bumbleflies.de/'),
                                              # Open Space
                                              ('Prinzipien', '/open-space-prinzipien-uebersicht'),
                                              ('Checkliste', '/open-space-checkliste'),
                                              ('Über uns', '/ueber-uns'),
                                              ])
    def test_navigation(self, bumbleserve, title, page, allowed_stylesheets, display, url):
        nav_links = query_site(bumbleserve, page).find_all('a', {'class': 'nav-link'})
        assert_link_present(display, url, nav_links, bumbleserve)

    @pytest.mark.parametrize('display, url', [('Impressum', '/impressum'),
                                              ('Datenschutzerklärung', '/datenschutz')])
    def test_legal(self, bumbleserve, title, page, allowed_stylesheets, display, url):
        legal_links = query_site(bumbleserve, page).find('ul', {'class': 'quicklinks'}).findChildren('a')
        assert_link_present(display, url, legal_links, bumbleserve)
