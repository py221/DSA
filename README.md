# DSA

Notes for Data Structure &amp; Algorithms

# Algos Warm-up

## Fibonacci Numbers

1. Naive Algo

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

2. Efficient Algo

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

## Big-O Notation

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
