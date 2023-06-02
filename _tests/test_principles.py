from typing import List

import bs4 as bs4
import pytest as pytest
from more_itertools import one

from _tests.helper import query_site

gallery_data = [
    ('Wer auch immer kommt', '/assets/img/os/1.jpg'),
    ('Was auch immer passiert', '/assets/img/os/2.jpg'),
    ('Es beginnt', '/assets/img/os/3.jpg'),
    ('Es ist vorbei', '/assets/img/os/4.jpg'),
    ('Wo auch immer', '/assets/img/os/5.jpg'),
    ('Wann immer du dich', '/assets/img/os/law.jpg'),
]


@pytest.mark.parametrize('text_start, image', gallery_data)
def test_all_principles_and_law_displayed(bumbleserve, text_start, image):
    principles: List[bs4.element.Tag] = query_site(bumbleserve, 'open-space-prinzipien-uebersicht').find(id='principles').findChildren(
        'div', {'class': 'col-md-4'})
    found_principle = one(
        filter(lambda t: t.find('div', {'class': 'text-muted'}).text.startswith(text_start), principles))

    assert found_principle.find('img').attrs['src'] == image
