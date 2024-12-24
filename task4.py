import pygame
import sys
import numpy as np

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры окна
width, height = 1000, 700
coef = 2
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Преобразование отрезка и его середины")

# Определяем цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)  # Исходный отрезок
BLUE = (0, 0, 255)  # Преобразованный отрезок
GREEN = (0, 255, 0)  # Середины отрезков

# Задаем координаты концов отрезка L
point1 = np.array([0, 100])
point2 = np.array([200, 300])

# Определяем матрицу преобразования T
T = np.array([[1, 2],
              [3, 1]])

# Применяем матричное преобразование к точкам
transformed_point1 = T @ point1
transformed_point2 = T @ point2

# Находим середины отрезков
midpoint1 = ((point1 + point2) / 2) // coef
midpoint2 = ((transformed_point1 + transformed_point2) / 2) // coef

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполняем экран белым цветом
    screen.fill(WHITE)

    # Рисуем исходный отрезок
    pygame.draw.line(screen, RED, point1 // coef, point2 // coef, 5)

    # Рисуем преобразованный отрезок
    pygame.draw.line(screen, BLUE, transformed_point1 // coef, transformed_point2 // coef, 5)

    # Рисуем середины отрезков
    pygame.draw.circle(screen, GREEN, tuple(midpoint1.astype(int)), 5)
    pygame.draw.circle(screen, GREEN, tuple(midpoint2.astype(int)), 5)

    # Соединяем середины отрезков
    pygame.draw.line(screen, GREEN, midpoint1.astype(int), midpoint2.astype(int), 2)

    # Обновляем экран
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()
