"""Greatest common divisor and least common multiple."""


def gcd_naive(a: int, b: int) -> int:
    """Try every candidate divisor. O(min(a, b)) time."""
    best = 0
    for d in range(1, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            best = d
    return best


def gcd(a: int, b: int) -> int:
    """Euclid's algorithm: gcd(a, b) = gcd(b, a mod b). O(log min(a, b)) steps."""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Least common multiple via  lcm(a, b) = a * b / gcd(a, b)."""
    if a == 0 or b == 0:
        return 0
    return a // gcd(a, b) * b  # divide first to keep the intermediate small


if __name__ == "__main__":
    x, y = (int(t) for t in input("a b: ").split())
    print(gcd(x, y), lcm(x, y))
