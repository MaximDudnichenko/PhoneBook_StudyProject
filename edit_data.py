# Модуль редактирования записи
# Подготовил Максим Дудниченко

def edit_data(key, card):
    for i in range(0,len(key)):
        print(i + 1, key[i], card[key[i]])
    edit_num = int(input('\nВведите номер поля, которое хотите изменить: ')) - 1
    card[key[edit_num]] = input('Введите новое значение: ')

    return card
