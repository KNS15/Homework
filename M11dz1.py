import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from PIL import Image

print('работа с библиотекой Pandas')
# 1 - создание класса объекта
s = pd.Series(np.arange(8), index=['a', 'b', 'c', 'd', 'какое-то число', 'f', 'g', 'конец'])
print(s)
#объект класса DataFrame
num_of_birth = dict(Friends=["Sashik", "Ondi", "Ilya"],
                    Day=[2, 29, 19], Month=[8, 9, 6],
                    Year=[1996, 1998, 1997])
num_of_birth = pd.DataFrame(num_of_birth)
print(num_of_birth)
print(type(num_of_birth["Friends"]))
print('работа с библиотекой matplotlib')
fig, ax = plt.subplots()

car = ["Golf", 'A3', 'A4', 'Jetta']
counts = [2, 1.5, 3.12, 1.84]
bar_labels = ['red', 'blue', 'gray', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:gray', 'tab:orange']

ax.bar(car, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('price car in million')
ax.set_title('Price car by kind and color')
ax.legend(title='car color')

plt.show()
print("выдан график на этом работа с этой библиотекой окончена")
print('работа с Библиотекой request')
r = requests.get('https://music.yandex.ru/home')
status_code = r.status_code
print(status_code)
print(r.headers)

print('работа с библиотекой pillow')
jp = Image.open("darth_vader.jpg")
print(jp.format, jp.size, jp.mode)
with Image.open("darth_vader.jpg") as jp:
    jp = jp.convert("L")
    jp.save('SW.png')



