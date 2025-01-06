# name = 'Алексей'
# print('Name: ', name)
# age = int(46)
# print('Age: ', age)
# new_age = int(age + 1)
# print('New Age: ' , new_age)
# is_student = True
# print('is Student: ', is_student)


# Number_of_completed_homework_assignments = 12
# Number_of_hours_spent = 1.5
# Course_title = "Python"
# Time_for_one_task = (Number_of_hours_spent / Number_of_completed_homework_assignments)
# print (Course_title, ", всего задач:", Number_of_completed_homework_assignments, ", затрачено часов:", Number_of_hours_spent, ", среднее время выполнения", Time_for_one_task, "часа")


# example = 'Топинамбур'
# print(example[0])
# print(example[-1])
# print(example[4:])
# print(example[::-1])
# print(example[1::2])


# my_string = input('Введите слово: ')
# print(len(my_string))
# print(my_string.upper())
# print(my_string.lower())
# print(my_string.replace(' ',''))
# print(my_string[0])
# print(my_string[-1])


# immutable_var = (12, 'Uraaa', '16', 333, True)
# print(immutable_var)
# mutable_list = [45, '909', False, 'xaxa']
# mutable_list[3] = 444
# print(mutable_list)


# my_dict = {'я': 1978, 'Лена': 1980, 'Настя': 1983 }
# print(my_dict)
# print(my_dict['я'])
# print(my_dict.get('она'))


# my_dict = { "Орешник" : 233445, "Тополь" : 132435, "Сармат" : 986532}
# print (my_dict)
# print (my_dict ["Тополь"])
# print (my_dict.get("Сатана"))
# print (my_dict.get("Сатана", 0))
# my_dict.update ({"Гладиолус" : 853609,
# "Ураган" : 476987})
# Deleted_value = my_dict.pop("Тополь")
# print (Deleted_value)
# print (my_dict)

# my_set = {3.14, "Пиндосы", 4, 9, 3.14, 9}
# print (my_set)
# my_set.add (5)
# print (my_set)
# my_set.add (2)
# print (my_set)
# # list = set(my_set)
# my_set.discard(3.14)
# print (my_set)

secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]

# ключ к расшифровке:
#   первое слово - 4-я буква
#   второе слово - буквы с 10 по 13, включительно
#   третье слово - буквы с 6 по 15, включительно, через одну
#   четвертое слово - буквы с 8 по 13, включительно, в обратном порядке
#   пятое слово - буквы с 17 по 21, включительно, в обратном порядке
#
# Требуется задать конкретные индексы, например secret_message[3][12:23:4]
# Если нужны вычисления и разные пробы - делайте это в консоли пайтона, тут нужен только результат

# вывести расшифрованное сообщение
print(secret_message[0][3])
print(secret_message[1][9:13])
print(secret_message[2][5:15:2])
print(secret_message[3][12:6:-1])
print(secret_message[4][20:15:-1])


