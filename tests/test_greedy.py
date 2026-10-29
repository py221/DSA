import itertools
import random

from car_fueling import min_refills
from covering_segments import min_points
from fractional_knapsack import max_loot_value
from largest_number import largest_number
from money_change import min_coins_greedy


def test_money_change():
    assert min_coins_greedy(2) == 2
    assert min_coins_greedy(28) == 6  # 10+10+5+1+1+1
    assert min_coins_greedy(0) == 0


def test_fractional_knapsack():
    assert max_loot_value([(60, 20), (100, 50), (120, 30)], 50) == 180.0
    assert abs(max_loot_value([(500, 30)], 10) - 500 / 3) < 1e-9
    assert max_loot_value([(10, 5)], 100) == 10.0


def test_car_fueling():
    assert min_refills(10, 3, [1, 2, 5, 9]) == -1
    assert min_refills(950, 400, [200, 375, 550, 750]) == 2
    assert min_refills(10, 3, [] ) == -1
    assert min_refills(5, 10, []) == 0


def _brute_refills(distance, tank, stops):
    best = -1
    for k in range(len(stops) + 1):
        for chosen in itertools.combinations(stops, k):
            pts = [0, *chosen, distance]
            if all(b - a <= tank for a, b in zip(pts, pts[1:])):
                return k
    return best


def test_car_fueling_random():
    rng = random.Random(3)
    for _ in range(300):
        distance = rng.randint(1, 20)
        stops = sorted(rng.sample(range(1, distance + 1), rng.randint(0, min(6, distance))))
        stops = [s for s in stops if s < distance]
        tank = rng.randint(1, 8)
        assert min_refills(distance, tank, stops) == _brute_refills(distance, tank, stops)


def test_covering_segments():
    assert min_points([(1, 3), (2, 5), (3, 6)]) == [3]
    assert min_points([(4, 7), (1, 3), (2, 5), (5, 6)]) == [3, 6]
    assert min_points([]) == []


def test_covering_segments_random():
    rng = random.Random(4)
    for _ in range(200):
        segs = []
        for _ in range(rng.randint(1, 6)):
            a = rng.randint(0, 10)
            segs.append((a, a + rng.randint(0, 4)))
        pts = min_points(segs)
        assert all(any(l <= p <= r for p in pts) for l, r in segs)
        universe = range(0, 15)
        for k in range(len(pts)):
            for combo in itertools.combinations(universe, k):
                assert not all(any(l <= p <= r for p in combo) for l, r in segs)


def test_largest_number():
    assert largest_number([21, 2]) == "221"
    assert largest_number([9, 4, 6, 1, 9]) == "99641"
    assert largest_number([23, 39, 92]) == "923923"
    rng = random.Random(5)
    for _ in range(200):
        nums = [rng.randint(0, 120) for _ in range(rng.randint(1, 5))]
        brute = max("".join(map(str, p)) for p in itertools.permutations(nums))
        # equal length strings, so lexicographic max equals numeric max
        assert largest_number(nums) == brute
