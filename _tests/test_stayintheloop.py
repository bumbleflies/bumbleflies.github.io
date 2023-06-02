from typing import List

import bs4 as bs4
import pytest as pytest
from more_itertools import one

from _tests.helper import query_site

def test_stayintheloop_has_google_form(bumbleserve):
    google_form= one(query_site(bumbleserve, 'informiert-bleiben').find(id='googleform').findChildren('iframe'))
    assert google_form['src'].startswith('https://docs.google.com/forms')
