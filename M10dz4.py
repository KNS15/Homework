from queue import Queue
from threading import Thread
from random import randint
from time import sleep
from itertools import zip_longest


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        rnd = randint(3, 10)
        sleep(rnd)


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        free_tables = list(filter(lambda t: t.guest is None, self.tables))
        guests_tables = zip_longest(guests, free_tables, fillvalue=None)
        for guest, table in guests_tables:
            if guest is not None:
                if table is not None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол № {table.number}')
                else:
                    self.queue.put(guest)
                    print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while True:
            occupied_tables = [t for t in self.tables if t.guest is not None]
            if self.queue.empty() and len(occupied_tables) == 0:
                print('Очередь рассосалась, все столы свободны')
                break
            for table in occupied_tables:
                if not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол № {table.number} освободился')
                    table.guest = None
                    if not self.queue.empty():
                        guest = self.queue.get()
                        table.guest = guest
                        print(f'{guest.name} дождался(ась) своей очереди и сел(-а) за стол № {table.number}')
                        guest.start()


tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang',
                'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina',
                'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
