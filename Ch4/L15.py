def main_func(nested_documents: dict, target_document_id: int, level: int=1) -> int:
    for doc in nested_documents:
        if doc == target_document_id:
            return level
        else:
            found = main_func(nested_documents.get(doc), target_document_id, level + 1)
            if found > 0:
                return found
    return -1
    


run_cases = [
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 2, 2),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 9, 4),
]

submit_cases = run_cases + [
    ({}, 1, -1),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 5, 4),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 20, -1),
]

'''
Assignment
Complete the count_nested_levels function. It takes a dictionary of nested documents, the target document id and the current level of the document.

1. Loop over document_ids in the nested_documents dictionary
    1. If the current document_id matches the target_document_id, return its level of nesting
    2. If the target_document_id is not found, recursively call count_nested_levels on the current document_id and increment the level
    3. If the recursive call found the target_document_id's level, return it
2. If the target_document_id doesn't exist, the function should return -1
'''

### Example
## In this dictionary, the document with id 3 is nested 2 levels deep. Document 2 is nested 1 level deep:
{
    1: {
        3: {}
    },
    2: {}
}