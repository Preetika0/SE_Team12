"""Branch coverage tests for food_delivery.py.

Run from this directory:
    coverage erase
    coverage run --branch --source=food_delivery -m pytest -q BranchCoverageTest_food_delivery_application.py
    coverage report -m
"""

import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


@pytest.mark.parametrize("distance", [0, -1, 16, 20])
def test_delivery_charge_invalid_distance_branches(distance):
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(distance, 100, False)


@pytest.mark.parametrize(
    "distance,order_value,raining,expected",
    [
        (2, 500, False, 0),    # free order: order_value >= 500
        (2, 499, False, 20),   # <= 3 km tier
        (3, 200, True, 50),    # boundary and rain surcharge
        (5, 200, False, 40),   # <= 8 km tier
        (8, 200, True, 70),    # boundary and rain surcharge
        (9, 200, False, 60),   # far tier
        (15, 200, True, 90),   # maximum valid distance
    ],
)
def test_delivery_charge_all_decisions(distance, order_value, raining, expected):
    assert delivery_charge(distance, order_value, raining) == expected


def test_apply_coupon_none_branch():
    assert apply_coupon(300, None, False) == 300


def test_apply_coupon_invalid_code_branch():
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "INVALID", True)


def test_apply_coupon_welcome_not_first_order_branch():
    with pytest.raises(ValueError, match="coupon only for first order"):
        apply_coupon(300, "WELCOME", False)


def test_apply_coupon_welcome_first_order_branch():
    assert apply_coupon(300, "WELCOME", True) == 200


def test_apply_coupon_low_order_value_branch():
    assert apply_coupon(150, "SAVE50", False) == 150


def test_apply_coupon_regular_discount_branch():
    assert apply_coupon(300, "SAVE50", False) == 250


@pytest.mark.parametrize(
    "distance,peak,busy,expected",
    [
        (5, False, False, 35),  # neither peak nor busy
        (5, True, False, 45),   # peak only
        (5, False, True, 50),   # busy only
        (5, True, True, 65),    # peak + busy + nested peak surcharge
    ],
)
def test_estimated_time_all_boolean_branches(distance, peak, busy, expected):
    assert estimated_time(distance, peak, busy) == expected
