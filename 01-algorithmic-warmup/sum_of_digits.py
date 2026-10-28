"""Tiny first exercises: adding numbers and summing digits."""


def sum_of_two(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


def digit_sum(n: int) -> int:
    """Sum of the decimal digits of |n|."""
    total = 0
    n = abs(n)
    while n:
        n, d = divmod(n, 10)
        total += d
    return total


if __name__ == "__main__":
    print(sum(int(t) for t in input().split()))
