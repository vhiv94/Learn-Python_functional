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

## Which line has the recursive call?
# print(n)
# if n == 0:
# else:
# *countdown(n - 1)

## What would happen if we swapped {countdown(n - 1)} with {countdown(n)} for n > 0?
# The code would be more elegant
# It will speed up the function execution
# *An infinite recursive loop