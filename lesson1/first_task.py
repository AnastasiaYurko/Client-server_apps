# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

str_format = ['разработка', 'сокет', 'декоратор']
unicode_format = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                  '\u0441\u043e\u043a\u0435\u0442',
                  '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']


def printing(arr):
    for word in arr:
        print(word)
        print(type(word))


printing(str_format)
printing(unicode_format)