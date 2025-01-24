def manual_difference(set1, set2):
    result = set()
    for item in set1:
        if item not in set2:
            result.add(item)
    return result

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

builtin_result = set_a.difference(set_b)
print("builtin", builtin_result)

custom_result = manual_difference(set_a, set_b)
print("Custom", custom_result)