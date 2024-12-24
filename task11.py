import numpy as np
import matplotlib.pyplot as plt

# Определяем начальные параметры
O = (60, 450)
UX = 60
UY = 60

# Функция для рисования осей
def draw_axes(x_min, x_max, y_min, y_max):
    plt.axhline(0, color='green', lw=1)
    plt.axvline(0, color='green', lw=1)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

# Функция для рисования многоугольника
def draw_polygon(vertices):
    polygon = plt.Polygon(vertices, fill=None, edgecolor='cyan')
    plt.gca().add_patch(polygon)

# Инициализация данных
N_points = 4
N = 2

L = np.zeros((N_points, N))
Lo = np.zeros((N_points, N))

L[0] = [2.0, 0.5]
L[1] = [8.0, 0.5]
L[2] = [8.0, 6.5]
L[3] = [2.0, 6.5]

p = 0.95
q = 1 - p
N_iterations = 50

# Настройка графика
plt.figure()
draw_axes(0.0, 8.0, 0.0, 7.0)

# Основной цикл
for k in range(1, N_iterations + 1):
    draw_polygon(L)

    # Вычисление новых координат
    Lo[0] = p * L[0] + q * L[1]
    Lo[1] = p * L[1] + q * L[2]
    Lo[2] = p * L[2] + q * L[3]
    Lo[3] = p * L[3] + q * L[0]

    # Копирование новых координат
    L = np.copy(Lo)
    plt.gca().set_facecolor((0, 1, 1, 0))  # Установка цвета фона

# Отображение графика
plt.gca().set_aspect('equal', adjustable='box')
plt.show(block=False)
plt.pause(5)  # Задержка перед закрытием
plt.close()
