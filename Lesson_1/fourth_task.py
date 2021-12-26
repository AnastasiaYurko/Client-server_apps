# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).

str_format = ['разработка', 'администрирование', 'protocol', 'standard']
str_to_bytes = []
bytes_to_str = []

for word in str_format:
    b = word.encode('utf-8')
    str_to_bytes.append(b)
    w = b.decode('utf-8')
    bytes_to_str.append(w)

for b in str_to_bytes:
    print(b)
    
print(bytes_to_str)

