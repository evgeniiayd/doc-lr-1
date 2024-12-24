import pygame
import numpy as np

# Инициализация Pygame
pygame.init()

# Настройки окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Визуализация преобразования отрезков')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Оригинальная матрица отрезков L (масштабирована на 100 для видимости)
L = np.array([[-1/2, 3/2],
              [3, -2],
              [-1, -1],
              [3, 5/3]]) * 50

# Матрица преобразования T
T = np.array([[1, 2],
              [1, -3]])

# Функция для применения матрицы преобразования T
def transform(segment, T):
    return np.dot(T, segment.T).T

# Функция для нахождения середины отрезка
def midpoint(segment):
    return (segment[0] + segment[1]) / 2

# Преобразование и смещение отрезков в видимую область
transformed_segments = []
for i in range(0, len(L), 2):
    segment = L[i:i+2]
    transformed_segment = transform(segment, T)
    # Смещение преобразованного отрезка в видимую область
    transformed_segment += np.array([[400], [300]])  # Сдвиг в центр окна
    transformed_segments.append(transformed_segment)

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение фона
    screen.fill(WHITE)

    # Рисование оригинальных отрезков
    for i in range(0, len(L), 2):
        pygame.draw.line(screen, BLACK, L[i] + [400, 300], L[i+1] + [400, 300], 2)


    # Рисование преобразованных отрезков
    for segment in transformed_segments:
        pygame.draw.line(screen, BLUE, segment[0], segment[1], 2)


    pygame.display.flip()

# Выход из Pygame
pygame.quit()



