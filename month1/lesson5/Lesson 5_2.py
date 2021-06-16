# Lesson 1
# eng_to_rus = {
#     "dog": "собака",
#     "cat": "кошка",
#     "book": "книга",
#     "table": "стол",
#     "continue": "продолжить",
#     "simple": "простой"
# }
#
# print(eng_to_rus["table"])
# print(eng_to_rus["simple"])
# print(eng_to_rus["cat"])


# Lesson 2
# eng_to_rus = {
#     "dog": "собака",
#     "cat": "кошка",
#     "book": "книга",
#     "table": "стол",
#     "continue": "продолжить",
#     "simple": "простой"
# }
# while True:
#     word = input("Слово для перевода: ")
#     print(eng_to_rus[word])


# Lesson 4
# eng_to_rus = {
#     "dog": "собака",
#     "cat": "кошка",
#     "book": "книга",
#     "table": "стол",
#     "continue": "продолжить",
#     "simple": "простой"
# }
# while True:
#     word = input("Слово для перевода: ")
#     try:
#         print(eng_to_rus[word])
#     except KeyError:
#         print("Слова нету в словаре")


# Lesson 5
# eng_to_rus = {
#     "dog": "собака",
#     "cat": "кошка",
#     "book": "книга",
#     "table": "стол",
#     "continue": "продолжить",
#     "simple": "простой"
# }
# rus_to_eng = {
#     "собака": "dog",
#     "кошка": "cat",
#     "книга": "book",
#     "стол": "table",
#     "продолжить": "continue",
#     "простой": "simple"
# }
# while True:
#     lang = input("Язык для перевода: ")
#     if lang == "eng":
#         word = input("Слово для перевода: ")
#         try:
#              print(eng_to_rus[word])
#         except KeyError:
#              print("Слова нету в словаре")
#
#     if lang == "rus":
#         word = input("Слово для перевода: ")
#         try:
#             print(rus_to_eng[word])
#         except KeyError:
#             print("Cлова нету в словаре")


# Lesson 6
# eng_to_rus = {
#     "dog": "собака",
#     "cat": "кошка",
#     "book": "книга",
#     "table": "стол",
#     "continue": "продолжить",
#     "simple": "простой"
# }
# rus_to_eng = {
#     "собака": "dog",
#     "кошка": "cat",
#     "книга": "book",
#     "стол": "table",
#     "продолжить": "continue",
#     "простой": "simple"
# }
# while True:
#     lang = input("Язык для перевода: ")
#     if lang == "eng":
#         word = input("Слово для перевода: ")
#         try:
#             print(eng_to_rus[word])
#         except KeyError:
#             print("Слова нету в словаре, хотите добавить? ")
#             option = input()
#             if option == "y":
#                 eng_to_rus[word] = input(f"Перевод для слова " + word)
#     if lang == "rus":
#         word = input("Слово для перевода: ")
#         try:
#             print("Слова нету в словаре, хотите добавить? ")
#             option = input()
#             if option == "y":
#                 rus_to_eng[word] = input(f"Перевод для слова " + word)
#         except KeyError:
#             print("Cлова нету в словаре")


# Lesson 7
# d = {
# "pet": ["питомец", "погладить по голове"],
# "let's gooo": ["поехали","погнали" ],
# "Fly": ["муха", "летать"]
# }
# word = d ['Fly']
# for i in range(len(word)):
#     print(f"Значение{i}: {word[i]}")



