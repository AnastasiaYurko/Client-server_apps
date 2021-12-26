# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку созданного файла (исходить из того, что вам априори неизвестна кодировка этого
# файла!). Затем открыть этот файл и вывести его содержимое на печать. ВАЖНО: файл должен быть открыт без ошибок вне
# зависимости от того, в какой кодировке он был создан!

from chardet import detect

f = open('test_file.txt', 'w', encoding='utf-8')
f.write('сетевое программирование \nсокет \nдекоратор')
f.close()

with open('test_file.txt', 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']
print('encoding: ', encoding)

with open('test_file.txt', encoding=encoding) as f_n:
    for el_str in f_n:
        print(el_str, end='')
    print()
