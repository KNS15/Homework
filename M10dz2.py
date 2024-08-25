import threading
from threading import Thread
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        while self.enemies > 0:
            days += 1
            self.enemies = self.enemies - self.power if self.enemies - self.power > 0 else 0
            print(f'{self.name} сражается {days} день(дня)..., осталось {self.enemies} воинов.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 33)
second_knight = Knight("Sir Galahad", 7)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')
