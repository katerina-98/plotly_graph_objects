import math
import numpy as np
import plotly.graph_objects as go


# Данные для оси x (значения от -10 до 10 с шагом 1)
x = list(np.arange(-9, 3, 0.2))

# Данные для оси y (значения функции y = 2x)
y = [math.cos(val) for val in x]

# Создание интерактивного линейного графика
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers'))

# Добавление подписей осей и заголовка
fig.update_layout(title='Интерактивный график функции y = 2x', xaxis_title='x', yaxis_title='y')

# Отображение графика
fig.show()
