"""Fractional knapsack: items can be taken in part."""


def max_loot_value(items: list[tuple[float, float]], capacity: float) -> float:
    """Maximum total value that fits in `capacity`.

    `items` is a list of (value, weight) pairs with positive weights. Items are
    taken in decreasing order of value per unit weight; the last one taken may
    be split.
    """
    total = 0.0
    for value, weight in sorted(items, key=lambda it: it[0] / it[1], reverse=True):
        if capacity <= 0:
            break
        take = min(weight, capacity)
        total += value * (take / weight)
        capacity -= take
    return total
