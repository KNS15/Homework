def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


random_numbers_for_my_practice = [49, 69, 89.05, 416, 823, 0.0001, 2024]
result = apply_all_func(random_numbers_for_my_practice, min, max, len, sum, sorted)
print(result)

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
