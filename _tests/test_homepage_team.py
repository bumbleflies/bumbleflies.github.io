from typing import List

import bs4 as bs4
import pytest as pytest
from more_itertools import one

from _tests.helper import query_site

member_data = [
    ('Christian Dähn', '/assets/img/team/1.webp', {
        'fa-twitter': 'https://twitter.com/da_chrisch',
        'fa-github': 'https://github.com/dachrisch',
        'fa-linkedin-in': 'https://www.linkedin.com/in/christiandaehn/'}),
    ('Sebastian Keller', '/assets/img/team/2.webp', {
        'fa-twitter': 'https://twitter.com/se_keller',
        'fa-linkedin-in': 'https://www.linkedin.com/in/sebastian-keller-166a83ba/'}),
    ('Christoph Kämpfe', '/assets/img/team/3.webp', {
        'fa-twitter': 'https://twitter.com/kaempfechris',
        'fa-linkedin-in': 'https://www.linkedin.com/in/christoph-k%C3%A4mpfe/'})
]


@pytest.mark.parametrize('name, image, social_links', member_data)
def test_team_member(bumbleserve, name, image, social_links):
    team_member: List[bs4.element.Tag] = query_site(bumbleserve).find(id='team').findChildren('div',
                                                                                              {'class': 'team-member'})
    found_member = one(filter(lambda t: t.find('h3').text == name, team_member))
    assert found_member

    assert found_member.find('img').attrs['src'] == image

    all_social_links = found_member.find('ul', {'class': 'social-buttons'}).findAll('a')
    for key, url in social_links.items():
        found_link: bs4.element.Tag = one(filter(lambda l: l.attrs['href'] == url, all_social_links))
        assert found_link
        assert found_link.find('i', {'class': key})
    print(found_member)
