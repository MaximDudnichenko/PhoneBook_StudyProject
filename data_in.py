# Модуль ввода записи
# Подготовил Дмитрий Хоняков
# Код-ревью Максим Дудниченко

def input_data(key):
    card = {}
    print('Введите следующие данные:')
    for i in range(0,len(key)):
        card[key[i]] = input(f'{key[i]}: ')

    return card
