"""Fewest refuelling stops on a straight road."""


def min_refills(distance: int, tank: int, stops: list[int]) -> int:
    """Minimum number of refills to drive `distance` with a full tank range of `tank`.

    `stops` are the positions of gas stations in increasing order. The car
    starts with a full tank. Returns -1 if the trip is impossible.

    Greedy rule: drive to the farthest station you can reach, refill there.
    """
    points = [0, *stops, distance]
    refills = 0
    current = 0  # index in `points` of where we last filled up
    for i in range(1, len(points)):
        if points[i] - points[i - 1] > tank:
            return -1
    while True:
        # farthest point reachable from `current`
        last = current
        while last + 1 < len(points) and points[last + 1] - points[current] <= tank:
            last += 1
        if last == len(points) - 1:
            return refills
        current = last
        refills += 1
