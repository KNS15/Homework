class Building:
    total = 0

    def __init__(self):
        Building.total += 1


for total in range(1, 41):
    x = Building()
    print(x.total)
