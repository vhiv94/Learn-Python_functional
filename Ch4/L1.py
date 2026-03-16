def main_func(x):
    if x <= 1:
        return 1
    return x * main_func(x - 1)

run_cases = [
    (3, 6),
    (5, 120),
    (0, 1),
]

submit_cases = run_cases + [
    (1, 1),
    (2, 2),
    (10, 3628800),
]

## Another Example
def print_chars(word, i):
    if i == len(word):
        return
    print(word[i])
    print_chars(word, i + 1)

print_chars("elephant", 3)
# H
# e
# l
# l
# o

## Lesson 2: What happens if a recursive function has no base case?
# It's no longer considered recursive
# *It will keep calling itself forever, resulting in an infinite loop
# Alan Turing comes back from the dead to haunt the author

## Lesson 3: What is printed if I call print_chars('elephant', 3)?
# phant
# elephant
# ele
# ant