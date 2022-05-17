# DSA

Notes for Data Structure &amp; Algorithms

# Algos Warm-up

## Fibonacci Numbers

1. <b><i>Naive Algo</b></i>

```python
if n<=1:
    return n
else:
    return Fib(n-1) + Fib(n-2)
```

> T(n) let = # lines code

-   T(n) f. Fib = 3 + T(n-2) + T(n-2)
-   for Fib(n-1) & Fib(n-2)...
    -   recalculations from scratch

2. <b><i> Efficient Algo </b></i>

-   recursive array to store values
-   avoid re-calculations

```python
Fib = [0,1]

def Fibonacci(n):
    for i in range(2, n):
        Fib.append(Fib[i-1] + Fib[i-2])

    return Fib[n-1]

>>> Fibonacci(10)
>>> 34
```

## Greatest Common Devisor

-   gcd(a, b) = greatest common devisor for a, b

### Naive

-   very slow if digits go up to 20+

```python
def NaiveGCD(a,b):
    best = 0
    for d in range(len(1, a+b)):
        if a % d == 0 and b % d == 0:
            best = d
        return d
```

```python
>>> start = time.time()
>>> print(NaiveGCD(357, 234))
>>> 3

>>> end = time.time()
>>> print(end - start)
>>> 0.0055548
```

### Efficient

-   <b>Euclidean Algo</b>
-   let a' be the remainder when a is divided by b
    -   gcd(a,b) = gcd(a', b) = gcd(b, a')

```python
def EuclidGCD(a,b):
    if b == 0:
        return a
    else:
        a_remainder = a % b
    return EuclidGCD(b, a_remainder)
```

```python
>>> start = time.time()
>>> print(EuclidGCD(357, 234))
>>> 3

>>> end = time.time()
>>> print(end - start)
>>> 0.0
```

## runtimes Notation

### Asymptotic Notation

-   How runtime scale w input size
    > n
    > root n
    > nlogn
    > n^2
    > 2^n

### Big-O Notation

-   f(n) = O(g(n)) / f <<= g

    -   f constants N and c exists such that for all n >= N, f(n) <= c\*g(n)

    -   f is Big-O of n

-   e.g.

    -   3n^2 + 5n + 2 = O(n^2)

    -   if n>=1 ... 3n^2 + 5n + 2 <= 3n^2 + 5n^2 + 2n^2 = 10n^2

# Greedy Algo

## Intro

## Money Change

## Max Value of the Loot

## Car Fueling

# Divide &amp; Conquer

## Search

## Polynomial Mmultiplcation

## Master Theorem

## Sorting

## Quick Sort

# Dynamic Programming

## change Probelm

## String Comparison

## Knapsack

## Placing Parentheses
