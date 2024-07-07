def custom_write(file_name, strings):
    strings_positions = {}

    for i in range(len(strings)):
        file = open(file_name, 'a', encoding='utf-8')
        string_start = file.tell()
        file.write(strings[i] + '\n')

        strings_positions.update({(i+1, string_start): strings[i]})
        file.close()

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for end_result in result.items():
    print(end_result)