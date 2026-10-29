# 02 - Greedy algorithms

A greedy algorithm builds a solution by repeatedly taking the choice that
looks best right now and never revisiting it. That is only correct when the
problem has a **safe move**: some optimal solution contains the greedy
choice, and what is left after making it is a smaller instance of the same
problem.

The proof pattern I kept using: take any optimal solution that disagrees
with the greedy choice, swap in the greedy choice, and show the result is no
worse.

## Money change (`money_change.py`)

Minimise the number of coins for an amount, with coins 1, 5 and 10. Take the
largest coin that fits, repeat. Safe because any optimum with five 1-coins
can swap them for one 5-coin, and two 5-coins for a 10-coin, using fewer coins.

Pitfall: this does *not* work for every coin set. With coins 1, 3, 4 and
amount 6, greedy gives 4+1+1 (3 coins) but 3+3 uses 2. That failure is the
motivation for dynamic programming in stage 04.

## Fractional knapsack (`fractional_knapsack.py`)

Items have a value and a weight and may be split. Sort by value per unit
weight and fill from the best ratio down. Safe move: the best-ratio item is
used as much as possible - if the optimum holds less of it, replacing some
lower-ratio material with it cannot decrease value. Time $O(n\log n)$ for the sort.

Pitfall: dividing by a zero weight, and forgetting that the *last* item may be
taken only partly. The 0/1 version (no splitting) is *not* greedy - see stage 04.

## Car fueling (`car_fueling.py`)

```
0 ----A------B--------C-----D------------ distance
 \____ tank range ____/
```

From the last refill point, drive to the farthest station still within range.
Never stopping earlier is safe, since any station before it can be skipped by
an exchange argument. First check that no gap between neighbouring stations
(including start and destination) exceeds the tank, otherwise answer $-1$.
Time $O(n)$.

Pitfall: counting the start and the destination as stations, and off-by-one
at the final leg.

## Covering segments with points (`covering_segments.py`)

Sort segments by right endpoint. Put a point at the right end of the first
segment; it covers every segment that starts at or before it. Skip those,
repeat. Placing the point at the right end is safe because it reaches as far
as possible while still hitting the segment that ends earliest.

```
 [---]
    [-----]        points at the right ends:
        [--]          ^    ^
              [---]
```

Time $O(n\log n)$. Pitfall: sorting by *left* endpoint looks natural but
breaks the argument.

## Largest number (`largest_number.py`)

Join numbers into the largest possible digit string. Sorting by value or by
first digit fails: for 9 and 98 the right order is "998", for 2 and 21 it is
"221". The safe comparison is pairwise: `a` goes before `b` when
`a+b > b+a` as strings. Time $O(n\log n)$ comparisons of short strings.

Pitfall: comparing numerically (`9 < 98`) instead of by the concatenation.

## Takeaways

- Greedy is short and fast, but correctness needs an argument, not a few examples.
- Random testing against a brute force (see `tools/stress_test.py`) is a cheap
  way to catch a wrong greedy rule.
