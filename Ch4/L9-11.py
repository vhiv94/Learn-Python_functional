## Recursion Review

# for item in tree:
#     for nested_item in item:
#         for nested_nested_item in nested_item:
#             for nested_nested_nested_item in nested_nested_item:
                # # ... WHEN DOES IT END???

## What makes it hard to loop over a tree?
# *You don't know the depth of the tree (number of nested levels)
# You don't know the breadth of the tree (number of items at each level)
# Trees have too many items in the initial list
# Loops are hard for my smooth brain