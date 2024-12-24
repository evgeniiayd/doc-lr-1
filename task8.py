import pygame
import numpy as np

# Инициализация Pygame
pygame.init()

# Настройки окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Отражение треугольника')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Оригинальная матрица отрезков L (масштабирована на 100 для видимости)
L = np.array([[8, 1],
              [7, 3],
              [6, 2]]) * 50

# Матрица преобразования T для отражения относительно линии y = x
T = np.array([[0, 1],
              [1, 0]])

# Функция для применения матрицы преобразования T
def transform(segment, T):
    return np.dot(T, segment.T).T

# Преобразование треугольника
transformed_triangle = transform(L, T)


# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение фона
    screen.fill(WHITE)

    # Рисование оригинального треугольника
    pygame.draw.polygon(screen, BLACK, L, 2)

    # Рисование преобразованного треугольника
    pygame.draw.polygon(screen, BLUE, transformed_triangle, 2)

    pygame.display.flip()

# Выход из Pygame
pygame.quit()
