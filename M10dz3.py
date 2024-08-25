import random
from threading import Lock
from threading import Thread
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()


    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)
            self.balance += amount
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {amount}. Баланс: {self.balance}')
            sleep(0.001)


    def take(self):
        for i in range(100):
            if not self.lock.locked():
                request = random.randint(50, 500)
                print(f'Запрос на {request}')
                if self.balance >= request:
                    self.balance -= request
                    print(f'Снятие: {request}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')
                i += 1
            sleep(0.001)


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')