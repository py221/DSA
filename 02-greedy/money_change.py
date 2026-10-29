"""Make change with the fewest coins when the denominations are 1, 5 and 10."""

DENOMINATIONS = (10, 5, 1)


def min_coins_greedy(amount: int, denominations: tuple[int, ...] = DENOMINATIONS) -> int:
    """Always take the largest coin that still fits.

    Correct for the denominations 1, 5, 10 (each divides the next). It is NOT
    correct for arbitrary coin sets - see 04-dynamic-programming/change_dp.py.
    """
    if amount < 0:
        raise ValueError("amount must be non-negative")
    count = 0
    for coin in sorted(denominations, reverse=True):
        count += amount // coin
        amount %= coin
    return count
