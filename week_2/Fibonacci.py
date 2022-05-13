#%%
Fib = [0,1]

def Fibonacci(n):
    for i in range(2, n):
        Fib.append(Fib[i-1] + Fib[i-2])
    
    return Fib[n-1]

Fibonacci(10)
# >>> 34

# %%
