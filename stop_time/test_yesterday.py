from datetime import datetime

from freezegun import freeze_time
from yesterday import yesterday


@freeze_time("1983-01-01")
def test_yesterday():
    assert yesterday() == datetime(1982, 12, 31)
