
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name, strings):
    string_position = {}
    f = open(file_name, 'w', encoding='utf-8')
    i = 1
    for line in strings:
        string_position[(i, f.tell())] = line
        f.write(line + '\n')
        i += 1
    f.close()
    return string_position


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

