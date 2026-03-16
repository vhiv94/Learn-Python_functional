## Consider the following function (assume n is a non-negative integer):
def countdown(n):
    print(n)
    if n == 0:
        return
    else:
        countdown(n - 1)

## Which line contains the base case?
# print(n)
# *if n == 0
# else
# countdown(n - 1)