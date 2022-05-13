#%%
# input_num = '1 543 432 452 423 242 56 8 7856 865'
# input_num = sorted([int(num) for num in input_num.split()], reverse=True)
# print(input_num[0], input_num[1])
#%%
def max_pairwise_product(input_num):
    input_num = sorted([int(num) for num in input_num.split()], reverse=True)
    return (input_num[0] * input_num[1])

if __name__ == '__main__':
    input_n = int(input())
    input_num = input()
    if len([int(num) for num in input_num.split()]) != int(input_n):
        pass
    else:
        print(max_pairwise_product(input_num))

# %%
