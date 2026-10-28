"""Largest product of two different elements of a list."""


def max_pairwise_product_naive(nums: list[int]) -> int:
    """Check every pair. O(n^2)."""
    best = None
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            p = nums[i] * nums[j]
            if best is None or p > best:
                best = p
    if best is None:
        raise ValueError("need at least two numbers")
    return best


def max_pairwise_product(nums: list[int]) -> int:
    """Product of the two largest values. O(n), no sorting.

    Assumes non-negative numbers (the classic setting). With negatives the
    product of the two smallest could win; see max_pairwise_product_signed.
    """
    if len(nums) < 2:
        raise ValueError("need at least two numbers")
    i = max(range(len(nums)), key=nums.__getitem__)
    j = max((k for k in range(len(nums)) if k != i), key=nums.__getitem__)
    return nums[i] * nums[j]


def max_pairwise_product_signed(nums: list[int]) -> int:
    """Handles negatives: best of (two largest) and (two smallest)."""
    if len(nums) < 2:
        raise ValueError("need at least two numbers")
    s = sorted(nums)
    return max(s[-1] * s[-2], s[0] * s[1])


if __name__ == "__main__":
    input()  # element count, not needed in Python
    print(max_pairwise_product([int(t) for t in input().split()]))
