class Building:
    def __init__(self, name, numberOfFloors, buildingType):
        self.name = name
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


b1 = Building("ZNAK", 9, "Многоэтажное здание")
b2 = Building("My House", 1, "Одноэтажное здание")
print(b1 == b2)
