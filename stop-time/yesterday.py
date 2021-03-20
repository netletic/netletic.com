from datetime import datetime
from datetime import timedelta

from freezegun import freeze_time


def yesterday():
    return datetime.today() - timedelta(days=1)


@freeze_time("1983-01-01")
def test_yesterday():
    assert yesterday() == datetime("1982-12-31")
