
#%%
def EuclideanGCD(x, y):

    if y == 0:
        return x
    
    return EuclideanGCD(y, x % y)


# %%
if __name__ == '__main__':
    a, b = [int(x) for x in input().split()]
    print(EuclideanGCD(a, b))
# %%
