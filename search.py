# Модуль поиска по справочнику
# Подготовила Ульяна Овчаренко
# Код-ревью Максим Дудниченко


def search(keys, list_phonebook):
    for i in range(len(keys)): 
        print(i+1, keys[i])
    search_key = int(input('\nВыберите номер поля, по которому нужно произвести поиск: ')) - 1
    find_text = input('\nВведите искомый текст: ')
    new_list = []
    for item in list_phonebook:
        if item[keys[search_key]].lower() == find_text.lower():
            new_list.append(item)
    return new_list
