import pygame
import numpy as np

# Инициализация Pygame
pygame.init()

# Настройки окна
width, height = 1000, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Вращение треугольника')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Оригинальная матрица отрезков L (масштабирована на 100 для видимости)
L = np.array([[3, -1],
              [4, 1],
              [2, 1]]) * 100

# Матрица преобразования T для вращения на 90 градусов против часовой стрелки
T = np.array([[0, 1],
              [-1, 0]])

# Функция для применения матрицы преобразования T
def transform(segment, T):
    return np.dot(T, segment.T).T

# Преобразование треугольника
transformed_triangle = transform(L, T)

# Смещение для видимости
offset = np.array([[400], [300]])  # Сдвиг в центр окна
L += offset.T
transformed_triangle += offset.T

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
