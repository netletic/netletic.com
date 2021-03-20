from datetime import datetime
from datetime import timedelta

import pytest
from freezegun import freeze_time

from parse_incomplete_date import parse_date_from_incomplete_string


@freeze_time("2020-03-03")
@pytest.mark.parametrize(
    "partial_date, expected",
    [
        ("THU OCT 02 14:07:47", datetime(2014, 10, 2, 14, 7, 47)),
        ("MON MAR 02 11:40:47", datetime(2020, 3, 2, 11, 40, 47)),
        ("TUE JAN 26 00:16:32", datetime(2016, 1, 26, 0, 16, 32)),
        ("WED JUN 28 17:03:26", datetime(2017, 6, 28, 17, 3, 26)),
        ("FRI NOV 30 10:55:55", datetime(2018, 11, 30, 10, 55, 55)),
        ("MON SEP 09 14:58:19", datetime(2019, 9, 9, 14, 58, 19)),
        ("MON FEB 29 13:37:00", datetime(2016, 2, 29, 13, 37, 0)),
    ],
)
def test_find_date_from_incomplete_string(partial_date, expected):
    assert parse_date_from_incomplete_string(partial_date) == expected
