from collections import Counter

import pytest
from loop import delta
from loop import get_rx_bytes
from loop import t1_file
from loop import t2_file


@pytest.fixture(scope="session")
def t1() -> Counter:
    return get_rx_bytes(t1_file)


@pytest.fixture(scope="session")
def t2() -> Counter:
    return get_rx_bytes(t2_file)


def test_delta(t1: Counter, t2: Counter):
    assert delta(t1, t2)[0] == ("1/1/35", 545871439)
