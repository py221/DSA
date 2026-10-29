"""Cover every segment with as few points as possible."""


def min_points(segments: list[tuple[int, int]]) -> list[int]:
    """Smallest set of points such that each closed segment [l, r] contains one.

    Sort by right endpoint; whenever the next segment is not yet covered,
    place a point at its right end.
    """
    points: list[int] = []
    for left, right in sorted(segments, key=lambda s: s[1]):
        if not points or points[-1] < left:
            points.append(right)
    return points
