class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name


class Plant:
    edible = False
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            Mammal.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            Mammal.fed = False


class Predator(Animal):
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            Predator.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            Predator.fed = False
            Predator.alive = False


class Flower(Plant):
    def __init__(self, name):
        Flower.edible = False
        self.name = name


class Fruit(Plant):
    def __init__(self, name):
        Fruit.edible = True
        self.name = name


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
