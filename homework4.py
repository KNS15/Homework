immutable_var = 1, 2, 'a', 'b'
print(immutable_var)
#immutable_var[0] = 5  # невозможно изменять объекты т.к. данный тип хранения данных неизменяемый
mutable_list = [1, 2, 3, "a", "b", "c"]
mutable_list[0] = 5
mutable_list[2] = "d"
mutable_list[-1] = 25
print(mutable_list)
