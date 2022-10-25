from art import *
import data_in
import transformations as trf
import logger as log
import search as s
import print_data as pd
import edit_data as ed
import os

def read_and_print(key):
    # чтение данных из файла
    strings_from_file = log.read_book()
    phonebook = []
    # преобразование данных из строки в список
    for i in range(len(strings_from_file)):
        read_card = trf.Search_transform(strings_from_file[i], key)
        phonebook.append(read_card)
    # вывод результата на экран
    pd.print_data(phonebook)
    return phonebook

def rewrite_file(phonebook):
    os.remove('Phonebook.txt')
    for card in phonebook:
        # преобразование данных в строку
        string_to_file = trf.Convert_to_write(card)
        # запись данных в файл
        log.writing_txt(string_to_file)


print(text2art("Phonebook", font='tarty1',chr_ignore=True))
print('\nЧто хотите сделать:\n 1 - добавить запись\n 2 - найти запись\n 3 - изменить запись\n 4 - удалить запись\n 5 - вывести записи на экран\n')
while True:
    option = int(input('Введите номер опции: '))
    if option < 1 or option > 5:
        print('Такого варианта нет, выберите снова: ')
    else:
        break

keys = ['Фамилия', 
    'Имя', 
    'Отчество', 
    'Дата рождения', 
    'Телефон', 
    'Адрес', 
    'Комментарий']

if option == 1: # Добавить запись
    # форма ввода данных
    card = data_in.input_data(keys)
    # преобразование данных в строку
    string_to_file = trf.Convert_to_write(card)
    # запись данных в файл
    log.writing_txt(string_to_file)
    # pd.print_data(card)

elif option == 2: # Поиск записей
    phonebook = read_and_print(keys)
    # поиск по параметрам
    search_list = s.search(keys, phonebook)
    # вывод результата поиска на экран
    pd.print_data(search_list)

elif option == 3: # Изменить запись
    phonebook = read_and_print(keys)
    edit_num = int(input('\nВведите номер записи, которую хотите изменить: ')) - 1
    phonebook[edit_num] = ed.edit_data(keys, phonebook[edit_num])
    pd.print_data(phonebook)
    rewrite_file(phonebook)
    
elif option == 4: # Удалить запись
    phonebook = read_and_print(keys)
    delete_num = int(input('\nВведите номер записи, которую хотите удалить: ')) - 1
    del phonebook[delete_num]
    pd.print_data(phonebook)
    rewrite_file(phonebook)

elif option == 5:
    phonebook = read_and_print(keys)
