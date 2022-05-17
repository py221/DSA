#%%
import time 

#%%
Fib = [0,1]

def Fibonacci(n):
    for i in range(2, n):
        Fib.append(Fib[i-1] + Fib[i-2])
    
    return Fib[n-1]

Fibonacci(10)
# >>> 34

# %%
def EuclidGCD(a,b):
    if b == 0:
        return a
    else:
        a_remainder = a % b
    return EuclidGCD(b, a_remainder)

def NaiveGCD(a,b):
    best = 0
    for d in range(1, a+b):
        if a % d == 0 and b % d == 0:
            best = d
    return best

start = time.time()
print(NaiveGCD(357, 234))
end = time.time()
print(end - start)

# %%
