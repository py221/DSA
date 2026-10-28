# Data structures and algorithms: a learning path

Worked notes and clean Python 3.12 solutions, in the order I studied them.
Each stage has a `notes.md` (the idea, why it works, complexity, pitfalls I
hit) next to the code, and every solution has tests.

```
01 warm-up  ->  02 greedy  ->  03 divide & conquer  ->  04 dynamic programming
   measure        safe local       split, solve,           remember sub-answers
   and speed up   choices          combine                 instead of recomputing
```

## The path

| stage | covers | key takeaway |
|---|---|---|
| [01-algorithmic-warmup](01-algorithmic-warmup/notes.md) | Fibonacci (naive, memoised, iterative, last digit, mod m via Pisano period), GCD/LCM, max pairwise product, Big-O | Naive recursion can be exponential; Euclid and modular arithmetic turn impossible inputs into trivial ones |
| [02-greedy](02-greedy/notes.md) | money change, fractional knapsack, car fueling, covering segments, largest number | Greedy needs a safe-move argument, not just examples |
| [03-divide-and-conquer](03-divide-and-conquer/notes.md) | binary search, majority element, 3-way quicksort, inversions, closest pair, Karatsuba, master theorem | Write the recurrence, then read the cost off the master theorem |
| [04-dynamic-programming](04-dynamic-programming/notes.md) | change problem, edit distance, LCS, 0/1 knapsack, expression parenthesisation, primitive calculator | Define the state precisely; the loop is the easy part |

`tools/stress_test.py` is a naive-versus-fast randomized tester: run a slow,
obviously correct solution and the fast one on thousands of small random
inputs and stop at the first disagreement. It caught most of my off-by-one
bugs.

## Running

```
python3.12 -m venv .venv && . .venv/bin/activate
pip install pytest
pytest                                  # all tests
python tools/stress_test.py --trials 500 --seed 0
```

Most solution files can also be run directly and read input from the terminal,
for example `python 01-algorithmic-warmup/gcd_lcm.py`.

## License

MIT
