"""Lab 7 - Fuzz testing with Hypothesis.

Contract being tested
---------------------
Each function must either return a normal result or reject bad input with a
ValueError.  Any other exception type (AttributeError, TypeError, IndexError,
OverflowError, ...) is an unhandled crash and counts as a failure.
"""
import string

from hypothesis import given, strategies as st

from food_delivery import parse_order, delivery_eta, coupon_discount


# ---------------------------------------------------------------------------
# Required fuzz tests: arbitrary text (or None) must never crash a function.
# ---------------------------------------------------------------------------
@given(st.text() | st.none())
def test_parse_order_no_crash(s):
    try:
        result = parse_order(s)
    except ValueError:
        return                      # clean rejection of bad input is fine
    assert isinstance(result, dict)
    assert all(isinstance(q, int) and q > 0 for q in result.values())


@given(st.text() | st.none())
def test_delivery_eta_no_crash(s):
    try:
        result = delivery_eta(s)
    except ValueError:
        return
    assert isinstance(result, int) and result >= 15


@given(st.text() | st.none())
def test_coupon_discount_no_crash(s):
    try:
        result = coupon_discount(s)
    except ValueError:
        return
    assert isinstance(result, int) and result >= 0


# ---------------------------------------------------------------------------
# Extra fuzz test: numeric inputs (floats incl. nan/inf, huge integers).
# Random text almost never produces "inf" or 1e999, so feed numbers directly.
# ---------------------------------------------------------------------------
@given(st.floats() | st.integers())
def test_delivery_eta_numeric_no_crash(d):
    try:
        result = delivery_eta(d)
    except ValueError:
        return
    assert isinstance(result, int) and result >= 15


# ---------------------------------------------------------------------------
# Valid-input properties: well-formed input must give the correct answer.
# ---------------------------------------------------------------------------
NAME = st.text(alphabet=string.ascii_letters + string.digits, min_size=1, max_size=10)


@given(st.dictionaries(NAME, st.integers(min_value=1, max_value=1000), min_size=1))
def test_parse_order_valid_roundtrip(order):
    csv = ",".join(f"{name}:{qty}" for name, qty in order.items())
    assert parse_order(csv) == order


@given(st.floats(min_value=0, max_value=1000))
def test_delivery_eta_valid_formula(d):
    assert delivery_eta(d) == int(15 + d * 4)


@given(st.integers(min_value=0, max_value=999999), st.sampled_from(["SAVE", "save", "Save"]))
def test_coupon_discount_valid(n, prefix):
    assert coupon_discount(f"{prefix}{n}") == n
