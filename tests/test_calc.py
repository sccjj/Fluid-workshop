import functions.calc as fc
import pytest


def test_negatives():
    assert fc.adivb(-10, -5) == 2, "two neg return pos "


def test_pos_neg():
    assert fc.adivb(-9, 3) == -3, "one pos one neg =one neg"


def test_pos():
    assert fc.adivb(35, 7) > 0, "two pos = one pos"


def test_type():
    assert isinstance(fc.adivb(5, 10), float), "minor by l;arger should be float"


def test_rational():
    assert fc.adivb(10, 3) == pytest.approx(3.33, 0.01), "10/3 should be 3.333"
