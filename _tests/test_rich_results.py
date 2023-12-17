import json
from json import JSONDecodeError

import pytest

from _tests.helper import query_site
from _tests.test_sitemap import all_pages


@pytest.fixture(scope='session')
def rich_results(bumbleserve, all_pages):
    all_pages_bs = list(map(lambda page: query_site(bumbleserve, page), all_pages))
    all_pages_bs_ld = list(map(lambda page: page.find(type='application/ld+json'), all_pages_bs))
    return filter(lambda page: page is not None, all_pages_bs_ld)


class TestRichResults:
    def test_rich_results_valid(self, rich_results):
        for rich_result in rich_results:
            try:
                json.loads(rich_result.text)
            except JSONDecodeError:
                print(rich_result)
                raise
