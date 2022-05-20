#%%
# Least common multiplier 
def EuclideanLCM(x, y):

    if 'x_lst' not in globals():
        global x_lst
        x_lst = []
    if 'y_lst' not in globals():
        global y_lst
        y_lst = []

    x_lst.append(x)
    y_lst.append(y)

    if y == 0:
        return int(x * (x_lst[0]/x) * (y_lst[0]/x))

    if 0 in y_lst:
        x_lst = []  
        y_lst = []
        x_lst.append(x)
        y_lst.append(y)

    return EuclideanLCM(y, x % y)

# %%
if __name__ == '__main__':
    a, b = [int(x) for x in input().split()]
    print(EuclideanLCM(a, b))
# %%
