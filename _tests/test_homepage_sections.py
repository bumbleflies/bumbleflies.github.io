import pytest as pytest
from more_itertools import one

from _tests.helper import query_site


@pytest.mark.parametrize('section, name', [('services', 'Leistungen'),
                                           ('customer', ''),
                                           ('about', 'Über uns'),
                                           ('team', 'Wir sind bumbleflies')
                                           ])
def test_sections(bumbleserve, section, name):
    sections = query_site(bumbleserve, '/').find_all('section')

    found_section = one(filter(lambda s: s.attrs['id'] == section, sections))

    found_heading = name and filter(lambda s: s.text == name, found_section.find_all('h2')) or not name
    assert found_section and found_heading
