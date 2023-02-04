# -*- coding: utf-8 -*-
from ..main import my_diff, my_sum


def test_my_sum() -> None:
    assert my_sum(1, 1) == 2

def test_my_sum2() -> None:
    assert my_sum(1, 2) == 3
