class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, floor):
        print(f"Привет, хочу паредставить вам наш {self.name}, в нем {self.number_of_floors} этажей")
        if (floor < 1) or (floor > self.number_of_floors):
            print(f"Такого этажа не существует {self.name}")
        else:
            for i in range(1, floor + 1):
                print(i, "Этаж,квартиры доступны для покупки ")


h1 = House("ЖК Znak", 12)
h2 = House("ЖК Калинка", 10)


h1.go_to(2)
h2.go_to(15)
