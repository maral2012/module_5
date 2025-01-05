class House:
    def __init__(self, name, number):
        self.name = name
        self.number_of_floors = number

    def go_to(self, new_floor):
        floor = 0
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого экажа не существует')
        else:
            for floor in range(new_floor):
                print(floor + 1)
h1 = House('ЖК Горский', 18)
h1.go_to(5)

