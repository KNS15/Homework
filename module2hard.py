import random

while 1 > 0:
    def number():
        numbers = range(3, 21)
        current_number = random.choice(numbers)
        return current_number


    break

print("Ваше число для подбора пароля", number())


def generate_password(pairs):
    result = ""
    for i in range(1, pairs):
        for j in range(i + 1, pairs + 1):
            if pairs % (i + j) == 0:
                result += str(i) + str(j)
    return result


n = int(input("Введите число для подбора пароля к двери данное вам выше: "))
password = generate_password(n)
print(password)
