from datetime import datetime

from yesterday_asof import yesterday


def test_yesterday():
    assert yesterday(asof=datetime(1983, 1, 1)) == datetime(1982, 12, 31)
