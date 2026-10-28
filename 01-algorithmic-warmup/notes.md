# 01 - Algorithmic warm-up

The first stage is about one habit: write the obvious solution, then ask how
its running time grows and whether the same answer can be had with less work.

## Fibonacci

$F(0)=0,\; F(1)=1,\; F(n)=F(n-1)+F(n-2)$.

**Naive recursion** (`fib_naive`). Let $T(n)$ be the number of operations.
Then $T(n) = T(n-1) + T(n-2) + c$, which grows like $F(n)$ itself, i.e.
exponentially (about $1.618^n$). The reason is repeated work:

```
                 F(5)
               /      \
           F(4)        F(3)
          /    \       /   \
       F(3)   F(2)  F(2)  F(1)
       / \
    F(2) F(1)        <- F(3), F(2) are recomputed from scratch
```

**Memoization** (`fib_memo`) stores each value the first time it is computed,
so every $F(k)$ is evaluated once: $O(n)$ time, $O(n)$ space.

**Iteration** (`fib_iter`) walks upward and keeps only two numbers:
$O(n)$ time, $O(1)$ space. This is the version to use.

Pitfall: an off-by-one when the list of stored values starts as `[0, 1]`.
Index $n$ must be returned, not index $n-1$.

### Last digit, and F(n) mod m for huge n

Only the remainder matters, so reduce after every addition:
$(a+b) \bmod m = ((a \bmod m)+(b \bmod m)) \bmod m$. Numbers stay small and
the loop is still $O(n)$.

For astronomically large $n$ use the **Pisano period**: the sequence
$F(i) \bmod m$ is periodic, and the period $\pi(m)$ is at most $6m$.
Find it by iterating until the pair $(0,1)$ shows up again, then
$F(n) \bmod m = F(n \bmod \pi(m)) \bmod m$. For $m=10$ the period is 60.

**Sums.** $\sum_{i=0}^{n} F(i) = F(n+2) - 1$, so the last digit of a sum of
Fibonacci numbers is a single modular Fibonacci call. A partial sum
$F(m)+\dots+F(n)$ is a difference of two such prefix sums.

Pitfall: the Pisano loop must start comparing *after* the first step;
checking the starting pair immediately returns period 0.

## GCD and LCM

`gcd_naive` tries every divisor up to $\min(a,b)$ - fine for small inputs,
hopeless for 20-digit numbers. Euclid's observation: if $a'$ is the remainder
of $a$ divided by $b$ then $\gcd(a,b)=\gcd(b,a')$.

```
gcd(357, 234) -> gcd(234, 123) -> gcd(123, 111) -> gcd(111, 12)
              -> gcd(12, 3)    -> gcd(3, 0)     = 3
```

Each two steps at least halve the larger number, so there are
$O(\log \min(a,b))$ steps. Then $\operatorname{lcm}(a,b)=\frac{a}{\gcd(a,b)}\cdot b$
(divide before multiplying to avoid needless big intermediates).

Pitfall: in the naive loop, `return` placed inside the `for` body ends the
search at the first divisor; it has to come after the loop. Another early
mistake was a global list used to carry state through recursion for LCM -
unnecessary once LCM is just GCD plus one division.

## Maximum pairwise product

Sorting works ($O(n \log n)$) but a single scan for the two largest values
is $O(n)$. Pitfall: find the index of the maximum first, then the maximum of
the *other* indices - otherwise a repeated value or a single large value gets
multiplied by itself. With negative numbers the two smallest values can win;
`max_pairwise_product_signed` covers that.

## Reading running time

Asymptotic notation describes how the cost scales with input size:
$\log n,\ \sqrt n,\ n,\ n\log n,\ n^2,\ 2^n$ (slow growth to fast).

**Big-O.** $f(n)=O(g(n))$ if there are constants $c$ and $N$ such that
$f(n)\le c\,g(n)$ for all $n\ge N$.

Example: $3n^2+5n+2 = O(n^2)$, because for $n\ge1$
$3n^2+5n+2 \le 3n^2+5n^2+2n^2 = 10n^2$.

Related: $\Omega$ is a lower bound, $\Theta$ means both. Constants and
lower-order terms are dropped, so Big-O says nothing about which of two
$O(n)$ programs is faster in practice - only how each scales.

## Complexity summary

| function | time | space |
|---|---|---|
| `fib_naive` | $O(\varphi^n)$ | $O(n)$ stack |
| `fib_memo`, `fib_iter` | $O(n)$ | $O(n)$ / $O(1)$ |
| `fib_mod` | $O(m)$ after finding the period | $O(1)$ |
| `gcd` | $O(\log \min(a,b))$ | $O(1)$ |
| `max_pairwise_product` | $O(n)$ | $O(1)$ |
