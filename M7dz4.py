team_num1 = 6
team_num2 = 6
score1 = int(input("сколько задач решила 1 команда "))
score2 = int(input("сколько задач решила 2 команда "))
team_time1 = 1552.512
team_time2 = 2153.31451
time_avg = 45.2
print("В команде Мастера кода участников: %s" % team_num1)
print('Итого сегодня в командах участников: %(t1)s, %(t2)s ' % {'t1': team_num1, 't2': team_num2})

print('Волшебники данных решила задач {}'.format(score2))
print('Волшебники данных решили задачи за {}'.format(team_time1))

print(f'Команды решили {score1} , {score2} задач')
if score1 > score2 or score1 == score2 and team_time1 > team_time2:
    challenge_result = "Победа команды Мастера кода!"
elif score1 < score2 or score2 == score1 and team_time1 < team_time2:
    challenge_result = "Победа команды Волшебники Данных!"
else:
    challenge_result = "Ничья!"
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {score1 + score2} задач, в среднем по {time_avg} секунду на задачу!')
