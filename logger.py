# Подготовил Беляев Александр
# Код-ревью Максим Дудниченко

# Модуль для логирования контактов
# Данный модуль записывает данные в файлы Phonebook.csv и Phonebook.txt поля как в модуле Дмитрия data_in.


def writing_txt(string):
    file = 'Phonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{string}\n')


def read_book():
    file = 'Phonebook.txt'
    with open(file, 'r', encoding='utf-8') as data:
        strings = data.readlines()
    return strings