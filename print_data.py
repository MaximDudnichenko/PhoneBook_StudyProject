# Модуль вывода телефонной книжки на экран в виде таблицы
# Подготовил Дмитрий Хоняков
# Код-ревью Максим Дудниченко


import pandas as pd

def print_data(book):
    df = pd.DataFrame(book, [i + 1 for i in range(len(book))])
    print(df)
