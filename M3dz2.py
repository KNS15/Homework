def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b = 25, c = [1, 2, 3])

values_list = [50, 100, 500]
values_dict = {'a' : 1, 'b' : 'строка', 'c' : True}
values_list_2 = ['посмотрим что получится', 88]


print_params(*values_list)
print_params(values_dict, b = 13, c = 'ого')
print_params(**values_dict)
print_params(*values_list_2, 42)
