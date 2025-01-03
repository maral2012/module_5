# roket = ['Тополь', 'Сармат', 'Сатана', 'Орешник']
# disstansion = [10000, 12000, 11000, 9000]
# roket_dist_zip = zip(roket, disstansion)
# roket_dist = dict(roket_dist_zip)
# print(roket_dist)

# def my_fn(a,b):
#     a = a + 1
#     c = a + b
#     return c
# # res = my_fn(3, 4)
# # print(res)
# print(my_fn(3, 4))print
# print(my_fn(4, 6))
# print(my_fn(1, 3))


# def merge_lists_to_dict(a, b):
#     # c = zip(a, b)
#     # c = dict(c)
#     # return c
#     return dict(zip(a, b))
# res = merge_lists_to_dict(['Леха', 'Лена', 'Настя'], [46, 44, 41])
# print(res)

# def merge_lists_to_dict(a, b):
#        return dict(zip(a, b))
# res = merge_lists_to_dict(a = ['Леха', 'Лена', 'Настя'], b =[46, 44, 41])
# print(res)
# res_2 = merge_lists_to_dict(['Леха'], b =[46, 44, 41])
# print(res_2)

# def update_car_info(**car):
#     car['is_available'] = True
#     return car
# print(update_car_info(brand = 'xXx', prise = 1000000))

# name = 'all adam'
# print(name.title())

# first_name = "вася"
# last_name = "петров"
# full_name = f"{first_name} {last_name}"
# print(f"Hello, {full_name.title()}!")

# first_name = "вася"
# last_name = "петров"
# full_name = f"{first_name} {last_name}"
# massage = f"Hello, {full_name.title()}!"
# print(massage)

# print("\tPython")

# print("Python\n\tлучший\nиз\n\tлучших")

# nostarch_url = 'https://nostarch.com'
# print(nostarch_url.removeprefix('https://'))

# universe_age = 14_000_000_000
# print(universe_age)

# bicycles = [ 'trek', ' cannondale', 'edline', 'specialized']
# message = f"My first bicycle was а {bicycles [0].title()}."
# print(message)

# motorcycles = [ 'honda' , 'yamaha' , 'suzuki']
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)

# motorcycles = [ 'honda' , 'yamaha' , 'suzuki']
# print(motorcycles)
# motorcycles.append('ducati')
# print(motorcycles)

# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert (0, 'ducati' )
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)

# motorcycles = [ 'honda', 'yamaha', 'suzuki']
# print(motorcycles)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# motorcycles = [ 'honda', 'yamaha', 'suzuki']
# last_owned = motorcycles.pop()
# print(f"The last motorcycle I owned was а {last_owned. title()}. ")

# motorcycles = [ 'honda', 'yamaha', 'suzuki']
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was а {first_owned.title()}.")

# motorcycles = [ 'honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)

# motorcycles = [ 'honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# too_expeпsive = 'ducati'
# motorcycles.remove(too_expeпsive)
# print(motorcycles)
# print(f"\nA {too_expeпsive.title()} is too expensive for me.")

# list_gost = ['Андрей', 'Василий', 'Петр']
# print(f"'Уважаемый {list_gost[0]}, приглшаем Вас в гости!")
# print(f"'Уважаемый {list_gost[1]}, приглшаем Вас в гости!")
# print(f"'Уважаемый {list_gost[2]}, приглшаем Вас в гости!")
# list_gost[1] = 'Иван'
# print(f"'Уважаемый {list_gost[1]}, приглшаем Вас в гости!")

# name = "\tEric Matthes\n"
# print("Unmodified:")
# print(name)
# print("\nUsing lstrip():")
# print(name.lstrip())
# print("\nUsing rstrip():")
# print(name.rstrip())
# print("\nUsing strip():")
# print(name.strip())

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort ()
# print(cars)

# cars = [ 'bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)

# cars = [ 'bmw', 'audi', 'toyota', 'subaru']
# print ( "Here is the original list: ")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars))
# print("\nHere is the original list again:")
# print(cars)

# cars = [ 'bmw', 'audi', 'toyota', 'subaru']
# print(cars)
# cars. reverse()
# print(cars)

# country = ['Филиппины', 'Марокко', 'Бали', 'Казахстан', 'Япония']
# print(country)
# print(sorted(country))
# print(country)
# print(sorted(country, reverse=True))
# print(country)
# country.reverse()
# print(country)
# country.reverse()
# print(country)
# country.sort()
# print(country)
# country.sort(reverse=True)
# print(country)

# motorcycles = [ 'honda', 'yamaha', 'suzuki']
# print(motorcycles[-1])


# magicians = [ 'alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)

# magicians = [ 'alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was а great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print("Thank you, everyone. That was а great magic show!")

# list_pizza = ['Пепперони', 'Три сыра', 'Каламбер']
# for live_pizza in list_pizza:
#     print(f"Я люблю пиццу {live_pizza}")
# print('Я очень люблю пиццу')

# for value in range(1,5):
#     print(value)

# numbers = list(range(1,6))
# print(numbers)

# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

# squares = []
# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# squares = [value**2 for value in range(1,11)]
# print(squares)

# for value in range(1,21):
#     print(value)

# numbers = list(range(1, 1_000_001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# for value in range(1,20,2):
#      print(value)

# for value in range(1,30,3):
#       print(value)

# squares = []
# for value in range(1,11):
#      square = value ** 3
#      squares.append(square)
# print(squares)

# squares = [value**3 for value in range(1,11)]
# print(squares)

# players = [ 'char les', 'martina', 'michael', 'florence', 'eli' ]
# print(players[0:3])

# players = [ 'charles', 'martiпa', 'michael', 'floreпce', 'eli']
# print(players[1:4])

# players = [ 'charles', 'martina', 'michael', 'florence' , 'eli']
# print(players[-3:])