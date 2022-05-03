import pytest

from pages.dashboard import DashBoardPage


def test_basic_usage(browser):

    WORD = 'master chief collection'
    CURRENT_URL = 'Explore'

    search_function = DashBoardPage(browser)
    search_function.load()
    search_function.search(WORD)
    assert search_function.see_results() == CURRENT_URL


