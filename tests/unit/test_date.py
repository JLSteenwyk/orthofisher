import pytest

from datetime import date
from pathlib import Path

from mipypro.mipypro import get_date

here = Path(__file__)

class TestDate(object):
    def test_date(self):
        ## setup
        
        i = int(5)

        ## execution
        today = get_date()
        expected_date = date.today()

        ## check results
        # test output types
        assert today == expected_date
