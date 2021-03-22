import os
from collections import Counter

import pytest
from loop import delta
from loop import get_rx_bytes


DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture()
def t2() -> Counter:
    return get_rx_bytes(os.path.join(DIR, "t2.txt"))


@pytest.fixture()
def t1() -> Counter:
    return get_rx_bytes(os.path.join(DIR, "t1.txt"))


def test_delta(t1: Counter, t2: Counter):
    assert delta(t1, t2)[0] == ("1/1/35", 545871439)
