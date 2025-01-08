import requests

# Отправка GET-запроса
response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()  # Преобразование ответа в JSON

# Вывод первых 5 постов
for post in data[:5]:
    print(f"Title: {post['title']}")


import pandas as pd

# Чтение данных из CSV-файла
df = pd.read_csv('data.csv')

# Вывод первых 5 строк
print(df.head())

# Простая агрегация: среднее значение по столбцу 'value'
average_value = df['value'].mean()
print(f"Average Value: {average_value}")

import matplotlib.pyplot as plt

# Данные для визуализации
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание линейного графика
plt.plot(x, y, color='blue', marker='o')
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()