first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(first) - len(second)
                for first, second in zip(first, second)
                if len(first) != len(second))


print(list(first_result))


second_result = (len(first[x]) == len(second[x]) for x in range(len(first)))


print(list(second_result))

