team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

print("В команде Мастера кода участников:%s" % (team1_num))
print( "Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

print("Команда Волшебники данных решила задач: {} !".format(score_2))
print( "Волшебники данных решили задачи за {} с !".format(team1_time))

print('количество решённых задач по командам: 'f'{score_1}' ' и ' f'{score_2}')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_resul = 'Победа команды Мастера кода!'

elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_resul = 'Победа команды Волшебники Данных!'

else:
    challenge_resul = 'Ничья!'
print('Результат битвы: 'f'{challenge_resul}''!')

print("Сегодня было решено: " f'{tasks_total}' " задач, в среднем по: " f'{time_avg}' " секунды на задачу!.")

