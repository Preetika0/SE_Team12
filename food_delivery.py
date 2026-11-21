"""Food delivery helpers (Lab 7 - corrected version).

Every function validates its input and raises ValueError with a clear message
when the input is invalid, instead of crashing with an unrelated exception
(AttributeError, TypeError, IndexError, OverflowError, ...).  main() catches
ValueError and reports the problem to the user.
"""
import math
import re

_COUPON_RE = re.compile(r"SAVE([0-9]{1,6})")
_QTY_RE = re.compile(r"[0-9]{1,6}")


def parse_order(items_csv):
    """Parse 'pizza:2,burger:1' into {'pizza': 2, 'burger': 1}."""
    if not isinstance(items_csv, str):
        raise ValueError("order must be text like 'pizza:2,burger:1'")
    if not items_csv.strip():
        raise ValueError("order is empty")

    order = {}
    for item in items_csv.split(','):
        parts = item.split(':')
        if len(parts) != 2:
            raise ValueError(f"invalid item {item!r}: expected name:qty")
        name, qty = parts[0].strip(), parts[1].strip()
        if not name:
            raise ValueError(f"invalid item {item!r}: item name is empty")
        if not _QTY_RE.fullmatch(qty) or int(qty) < 1:
            raise ValueError(f"invalid quantity {qty!r}: must be a whole number >= 1")
        order[name] = int(qty)
    return order


def delivery_eta(distance_km):
    """Return the delivery time in minutes for a distance in km."""
    try:
        distance = float(distance_km)
    except (TypeError, ValueError, OverflowError):
        raise ValueError(f"invalid distance {distance_km!r}: must be a number")
    if not math.isfinite(distance) or distance < 0:
        raise ValueError(f"invalid distance {distance_km!r}: must be a finite number >= 0")
    eta = 15 + distance * 4
    if not math.isfinite(eta):
        raise ValueError(f"invalid distance {distance_km!r}: too large")
    return int(eta)


def coupon_discount(code):
    """Return the discount for a code like 'SAVE50' (case-insensitive)."""
    if not isinstance(code, str):
        raise ValueError("coupon code must be text like 'SAVE50'")
    match = _COUPON_RE.fullmatch(code.strip().upper())
    if match is None:
        raise ValueError(f"invalid coupon code {code!r}: expected SAVE<number>")
    return int(match.group(1))


def main():
    print("==== Running parse_order ====")
    user_input = input("Enter items as name:qty CSV (e.g. pizza:2,burger:1): ")
    try:
        print("Order:", parse_order(user_input))
    except ValueError as e:
        print("Invalid input:", e)

    print("\n==== Running delivery_eta ====")
    user_input = input("Enter distance in km (e.g. 4.5): ")
    try:
        print("ETA in Minutes:", delivery_eta(user_input))
    except ValueError as e:
        print("Invalid input:", e)

    print("\n==== Running coupon_discount ====")
    user_input = input("Enter a coupon code (e.g. SAVE50): ")
    try:
        print("Discount:", coupon_discount(user_input))
    except ValueError as e:
        print("Invalid input:", e)


if __name__ == "__main__":
    main()
