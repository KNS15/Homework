file_name = 'dz2.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line)
print(file.closed)
# Оператор With он автоматически закрывает файл, с которым ведется работа