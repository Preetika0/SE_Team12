"""Line/code coverage tests for food_delivery.py.

Run from this directory:
    coverage erase
    coverage run --source=food_delivery -m pytest -q CodeCoverageTest_food_delivery_application.py
    coverage report -m
"""

import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


def test_delivery_charge_rejects_out_of_range_distance():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(0, 250, False)
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(16, 250, False)


def test_delivery_charge_free_order_and_rain():
    assert delivery_charge(2, 500, True) == 30


def test_delivery_charge_distance_tiers():
    assert delivery_charge(2, 200, False) == 20
    assert delivery_charge(5, 200, False) == 40
    assert delivery_charge(10, 200, False) == 60


def test_coupon_none_and_valid_coupon():
    assert apply_coupon(300, None, False) == 300
    assert apply_coupon(300, "SAVE50", False) == 250
    assert apply_coupon(300, "WELCOME", True) == 200


def test_coupon_validation_and_minimum_order():
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "UNKNOWN", True)
    with pytest.raises(ValueError, match="coupon only for first order"):
        apply_coupon(300, "WELCOME", False)
    assert apply_coupon(150, "SAVE50", False) == 150


def test_estimated_time_all_adjustments():
    assert estimated_time(5, True, True) == 65
    assert estimated_time(2, False, False) == 23
