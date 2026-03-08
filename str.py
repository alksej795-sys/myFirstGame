""" Строковые типы (str):

Последовательность символов внутри кавычек (одинарных или двойных).
Примеры:
"""
s1 = "Привет, мир!"
s2 = 'Python'


# upper(): Преобразует все символы строки в верхний регистр.

text = "Привет, мир!"
upper_text = text.upper()  # upper_text = "ПРИВЕТ, МИР!"
print(upper_text)

# lower(): Преобразует все символы строки в нижний регистр.
 
message = "Python"
lower_message = message.lower()  # lower_message = "python"


# count(): Возвращает количество вхождений подстроки в строке.

sentence = "Python - прекрасный язык программирования, Python!"
count_python = sentence.count("Python")  # count_python = 2


# replace(): Заменяет все вхождения одной подстроки на другую.

phrase = "Я люблю Python"
updated_phrase = phrase.replace("Python", "программирование")  # updated_phrase = "Я люблю программирование"


#Получение подстроки с определенным диапазоном индексов.

text = "Python Programming"
substring = text[0:6]  # substring = 'Python'


#Обращение строки.

word = "hello"
reversed_word = word[::-1]  # reversed_word = 'olleh'




