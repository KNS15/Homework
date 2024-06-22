class Vehicle:
    vehicle_type = None


class Car:
    price = 1000000

    def horse_powers(self):
        return f'Мощность двигателя {self.horse_powers()}'


class Nissan(Vehicle, Car):
    price = 4000000
    vehicle_type = "Sport car"
    horse_powers = 813


nissan_gtr = Nissan()
print('Тип машины: ', nissan_gtr.vehicle_type)
print('Цена автомобиля: ', nissan_gtr.price)
