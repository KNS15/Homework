def test(value, *types, car_name="Audi_RS3", **values):
    print("этот тип параметра: ", type(value))
    print("Название модели и старна производитель:", values)
    for key, value in values.items():
        print(key, value)
    print(types)


test(1, "строка просто так", car_name="Audi", model_name="RS3", country="Germany")


def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n - 1)


print(factorial_recursive(8))
