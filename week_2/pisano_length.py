#%%
def pisano_length(m):
    i=2
    while(fib(i)%m!=0):
        i+=1
    if(fib(i+1)%m!=1):
        while(fib(i+1)%m!=1):
            i+=i
    print("The pisano length for mod {} is: {}".format(m,i))
    return(i)
def fib(n):
    a,b=0,1
    if(n==0 or n==1):
        return n
    else:
        for i in range(2,n+1):
            b,a=a+b,b
    return(b)
# %%
