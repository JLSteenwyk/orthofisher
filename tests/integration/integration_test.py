import pytest
import sys

from datetime import date
from mock import patch, call
from pathlib import Path

from mipypro.mipypro import main

here = Path(__file__)


@pytest.mark.integration
class TestIntegration(object):
    @patch("builtins.print")
    def test_integration(self, mocked_print):
        """
        test integration
        """

        today = date.today()
        expected_content = f"Hello world. Today is {today}"

        with patch.object(sys, "argv"):
            main()

        assert mocked_print.mock_calls == [call(expected_content)]