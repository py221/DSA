"""Fibonacci numbers: naive recursion, memoization, iteration, and modular tricks."""

from functools import cache


def fib_naive(n: int) -> int:
    """Plain recursion straight from the definition. Exponential time."""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n: int) -> int:
    """Recursion that remembers every value it has computed. O(n) time."""

    def go(k: int) -> int:
        if k <= 1:
            return k
        return memoized(k - 1) + memoized(k - 2)

    memoized = cache(go)
    return memoized(n)


def fib_iter(n: int) -> int:
    """Bottom-up iteration keeping only the last two values. O(n) time, O(1) space."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_last_digit(n: int) -> int:
    """Last decimal digit of F(n); reducing mod 10 at each step keeps numbers tiny."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % 10
    return a


def pisano_period(m: int) -> int:
    """Length of the cycle of Fibonacci numbers taken mod m (m >= 2).

    The pair (F(i) mod m, F(i+1) mod m) first returns to (0, 1) exactly one
    period after the start. The period never exceeds 6m.
    """
    if m < 2:
        raise ValueError("m must be at least 2")
    prev, cur = 0, 1
    for i in range(1, 6 * m + 1):
        prev, cur = cur, (prev + cur) % m
        if prev == 0 and cur == 1:
            return i
    raise AssertionError("unreachable: period is at most 6m")


def fib_mod(n: int, m: int) -> int:
    """F(n) mod m for very large n, using the Pisano period to shrink n."""
    if m == 1:
        return 0
    return fib_iter(n % pisano_period(m)) % m


def fib_sum_last_digit(n: int) -> int:
    """Last digit of F(0) + F(1) + ... + F(n).

    Uses the identity  F(0) + ... + F(n) = F(n + 2) - 1  and the fact that
    the last digit repeats with period 60.
    """
    return (fib_mod(n + 2, 10) - 1) % 10


def fib_partial_sum_last_digit(m: int, n: int) -> int:
    """Last digit of F(m) + F(m+1) + ... + F(n) for 0 <= m <= n."""
    if m > n:
        raise ValueError("m must not exceed n")
    return (fib_sum_last_digit(n) - (fib_sum_last_digit(m - 1) if m > 0 else 0)) % 10


if __name__ == "__main__":
    n = int(input("n: "))
    print(fib_iter(n))
