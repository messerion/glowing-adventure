first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(f) - len(s) for f,s in zip( first , second) if not len(f) == len(s))
print(list(first_result))

second_result = (len(first[i]) == len(second[i]) for i in range(0, len(first)))
print(list(second_result))