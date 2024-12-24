import pygame
import numpy as np

# Инициализация Pygame
pygame.init()

# Настройки окна
width, height = 1300, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Масштабирование треугольника')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Оригинальная матрица отрезков L (масштабирована на 100 для видимости)
L = np.array([[5, 1],
              [5, 2],
              [3, 2]]) * 100

# Матрица преобразования T для масштабирования в 2 раза
T = np.array([[2, 0],
              [0, 2]])

# Функция для применения матрицы преобразования T
def transform(segment, T):
    return np.dot(T, segment.T).T

# Преобразование треугольника
scaled_triangle = transform(L, T)

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

    # Рисование масштабированного треугольника
    pygame.draw.polygon(screen, BLUE, scaled_triangle, 2)

    pygame.display.flip()

# Выход из Pygame
pygame.quit()
