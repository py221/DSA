"""Arrange numbers so that their concatenation is as large as possible."""

from functools import cmp_to_key


def _compare(a: str, b: str) -> int:
    # a goes first if "ab" > "ba"
    return -1 if a + b > b + a else (1 if a + b < b + a else 0)


def largest_number(nums: list[int]) -> str:
    """Return the biggest number (as a string) formed by joining all of `nums`."""
    parts = sorted((str(n) for n in nums), key=cmp_to_key(_compare))
    return "".join(parts)
