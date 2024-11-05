def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [5,]
values_dict = {"b": 13, "c": 21}

values_list_2 = [54.32, 'Строка']

print_params()
print_params(*values_list, **values_dict)
print_params(*values_list_2, 42)




