# 2. Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом,
# а не ручном режиме с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя методы
# encode и decode) и определить тип, содержимое и длину соответствующих переменных.

str_format = ['class', 'function', 'method']
byte_format = []

for word in str_format:
    print(type(word))
    b = eval(f"b'{word}'")
    byte_format.append(b)

for b in byte_format:
    print(f"Тип переменной: {type(b)} /n Содержимое: {b} /n Длина: {len(b)}")


