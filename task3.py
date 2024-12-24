import pygame
import sys
import numpy as np

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Преобразование отрезка")

# Определяем цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)  # Исходный отрезок
BLUE = (0, 0, 255)  # Преобразованный отрезок

# Задаем координаты двух точек отрезка
point1 = np.array([2, 15])
point2 = np.array([6, 45])

# Определяем матрицу преобразования T
T = np.array([[1, 3],
              [4, 1]])

# Применяем матричное преобразование к точкам
transformed_point1 = T @ point1
transformed_point2 = T @ point2

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполняем экран белым цветом
    screen.fill(WHITE)

    # Рисуем исходный отрезок
    pygame.draw.line(screen, RED, point1, point2, 5)

    # Рисуем преобразованный отрезок
    pygame.draw.line(screen, BLUE, transformed_point1, transformed_point2, 5)

    # Обновляем экран
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()
