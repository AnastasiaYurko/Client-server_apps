"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать
скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). В это словаре параметров обязательно должны присутствовать
юникод-символы, отсутствующие в кодировке ASCII.
Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину
отступа в 4 пробельных символа;
Необходимо также установить возможность отображения символов юникода: ensure_ascii=False;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import os
import json

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def write_order_to_json(item, quantity, price, buyer, date):
    filename = os.path.join(CURRENT_DIR, 'orders.json')

    if os.path.exists(filename):
        data = {}

        with open(filename, encoding="utf-8") as fl:
            data = json.loads(fl.read())

        data['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})

        with open(filename, "w", encoding="utf-8") as fl:
            json.dump(data, fl, indent=4, separators=(',', ': '), ensure_ascii=False)

        print(f'Данные добавлены в {filename}')

    else:
        print(f'Исходный файл по пути {filename} не найден')


if __name__ == '__main__':
    write_order_to_json('Молоко', '1', '80', 'Александр П.', '09.01.2022')
    write_order_to_json('Творог', '3', '50', 'Александр П.', '09.01.2022')
    write_order_to_json('Сосиски', '1', '170', 'Александр П.', '09.01.2022')
    write_order_to_json('Макароны', '2', '40', 'Александр П.', '09.01.2022')
