import math
import random

import pytest

from fibonacci import (
    fib_iter,
    fib_last_digit,
    fib_memo,
    fib_mod,
    fib_naive,
    fib_partial_sum_last_digit,
    fib_sum_last_digit,
    pisano_period,
)
from gcd_lcm import gcd, gcd_naive, lcm
from max_pairwise_product import (
    max_pairwise_product,
    max_pairwise_product_naive,
    max_pairwise_product_signed,
)
from sum_of_digits import digit_sum, sum_of_two

KNOWN = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_fib_variants_agree_with_known_values():
    for n, expected in enumerate(KNOWN):
        assert fib_naive(n) == fib_memo(n) == fib_iter(n) == expected


def test_fib_large():
    assert fib_iter(100) == 354224848179261915075
    assert fib_memo(300) == fib_iter(300)


def test_last_digit():
    for n in range(200):
        assert fib_last_digit(n) == fib_iter(n) % 10
    assert fib_last_digit(331) == 9


def test_pisano_known_periods():
    assert pisano_period(2) == 3
    assert pisano_period(3) == 8
    assert pisano_period(10) == 60
    with pytest.raises(ValueError):
        pisano_period(1)


def test_fib_mod():
    for m in range(1, 30):
        for n in range(80):
            assert fib_mod(n, m) == fib_iter(n) % m
    assert fib_mod(10**18, 2) == fib_mod(10**18 % 3, 2)


def test_sums():
    for n in range(100):
        assert fib_sum_last_digit(n) == sum(fib_iter(i) for i in range(n + 1)) % 10
    for m in range(0, 30):
        for n in range(m, 40):
            expected = sum(fib_iter(i) for i in range(m, n + 1)) % 10
            assert fib_partial_sum_last_digit(m, n) == expected
    with pytest.raises(ValueError):
        fib_partial_sum_last_digit(5, 2)


def test_gcd_lcm():
    assert gcd(357, 234) == 3 == gcd_naive(357, 234)
    assert gcd(7, 0) == 7
    rng = random.Random(1)
    for _ in range(200):
        a, b = rng.randint(1, 500), rng.randint(1, 500)
        assert gcd(a, b) == gcd_naive(a, b) == math.gcd(a, b)
        assert lcm(a, b) == math.lcm(a, b)
    assert lcm(0, 5) == 0


def test_max_pairwise_product():
    assert max_pairwise_product([1, 2, 3]) == 6
    assert max_pairwise_product([5, 5]) == 25
    assert max_pairwise_product([7, 1, 1]) == 7
    rng = random.Random(2)
    for _ in range(200):
        nums = [rng.randint(0, 50) for _ in range(rng.randint(2, 8))]
        assert max_pairwise_product(nums) == max_pairwise_product_naive(nums)
        signed = [rng.randint(-50, 50) for _ in range(rng.randint(2, 8))]
        assert max_pairwise_product_signed(signed) == max_pairwise_product_naive(signed)
    with pytest.raises(ValueError):
        max_pairwise_product([1])


def test_sums_of_digits():
    assert sum_of_two(2, 3) == 5
    assert digit_sum(0) == 0
    assert digit_sum(-1234) == 10
