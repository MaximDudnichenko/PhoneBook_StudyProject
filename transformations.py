# Модуль написал Виталий Лушников
# Код-ревью Максим Дудниченко

# преобразование информации для записи в файл
# функция принимает словарь
def Convert_to_write(dict_user):
    result_string = ''
    string = ''
    # проход по значениям словаря
    for key, val in dict_user.items():
        if val != '':
            string += str(val) + '|'
        else:
            string += 'None|'
        # удаление разделителя в конце строки
        result_string = string[:-1]

    return result_string


# преобразование инф для поиска
# функция принимает строку с разделителями
def Search_transform(string_user, key):
    user_str = string_user.split('|')
    dict_user = {}
    # формирование словаря для поиска информации
    for i in range(len(key)):
        if user_str[i] == 'None' or user_str[i] == 'None\n':
            dict_user[key[i]] = ''
        else:    
            dict_user[key[i]] = user_str[i]
    dict_user[key[i]] = dict_user[key[i]][:-1]
    
    return dict_user
