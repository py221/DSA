#%%
def fib_last_digit(n):

    def __init_memo():
        global memo
        memo = []
        for i in range(n+1):
            memo.append(-1)

    if 'memo' not in globals():
        __init_memo()
        memo[0] = 0
        memo[1] = 1
        
    if len(memo) <= n+1 :
        for i in range(len(memo), n+1):
            memo.append(-1)

    if n == 0:
        return 0
    if n == 1:
        return 1

    if memo[n] != -1:
        return memo[n]

    memo[n] = (fib_last_digit(n-1) + fib_last_digit(n-2)) % 10
    return memo[n]

#%%
def fib_sum_last_digit(n):
    fib_last_digit(n)
    sum_arr = [sum(memo[0:i+1]) % 10 for i in range(len(memo))]
    return sum_arr[n]
    
# %%
if __name__ == '__main__':
    n = int(input())
    print(fib_last_digit(n))
    