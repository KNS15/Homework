def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res > 1:
            for i in range(2, int(res ** 0.5) + 1):
                if res % i == 0:
                    return "Составное"
                return 'Простое'

    return wrapper


@is_prime
def sum_three(*args):
    print(sum(args))
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
