
"""Feedback calculation for the Mastermind game."""

from collections import Counter


def feedback(code, guess):
    """Return the number of exact and partial matches."""

    # Count exact matches first.
    exact = sum(
        secret == attempted
        for secret, attempted in zip(code, guess)
    )

    # Remove exact positions before counting partial matches.
    remaining_code = Counter(
        secret
        for secret, attempted in zip(code, guess)
        if secret != attempted
    )

    remaining_guess = Counter(
        attempted
        for secret, attempted in zip(code, guess)
        if secret != attempted
    )

    # Each remaining symbol can match only once.
    partial = sum(
        min(count, remaining_guess[symbol])
        for symbol, count in remaining_code.items()
    )

    return exact, partial
