# 3. Определить, какие из слов, поданных на вход программы, невозможно записать в байтовом типе.
# Для проверки правильности работы кода используйте значения: «attribute», «класс», «функция», «type»

str_format = ['attribute', 'класс', 'функция', 'type']
byte_format = []
non_byte_format = []

for word in str_format:
    try:
        b = eval(f"b'{word}'")
        byte_format.append(b)
    except SyntaxError:
        non_byte_format.append(word)

print(f"Слова в байтовом типе: {byte_format}")
print(f"Слова, которые невозможно записать в байтовом типе: {non_byte_format}")
