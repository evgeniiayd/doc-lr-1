import pygame
import numpy as np

# Инициализация Pygame
pygame.init()

# Настройки окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Visualization of Segments and Transformations')
coef = 5

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Матрица преобразования T
T = np.array([[1, 2],
              [3, 1]])

# Определение двух параллельных отрезков
L = np.array([[50, 100],
              [250, 200],
              [50, 200],
              [250, 300]])

# Функция для применения матрицы преобразования
def transform(segment, T):
    return np.dot(T, segment.T).T

# Найти середину отрезка
def midpoint(segment):
    return (segment[0] + segment[1]) / 2

# Преобразовать отрезки
transformed_segments = []
for i in range(0, len(L), 2):
    segment = L[i:i+2]
    transformed_segment = transform(segment, T)
    transformed_segments.append(transformed_segment)

# Найти середины
midpoints = [midpoint(segment) for segment in transformed_segments]

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливка фона
    screen.fill(WHITE)

    # Рисуем исходные отрезки
    for i in range(0, len(L), 2):
        pygame.draw.line(screen, BLACK, L[i] // coef, L[i+1] // coef, 2)
        mid = midpoint(L[i:i+2])
        pygame.draw.circle(screen, RED, (int(mid[0]) // coef, int(mid[1] // coef)), 5)  # Середина отрезка

    # Рисуем преобразованные отрезки
    for segment in transformed_segments:
        pygame.draw.line(screen, BLUE, segment[0] // coef, segment[1] // coef, 2)
        mid = midpoint(segment)
        pygame.draw.circle(screen, RED, (int(mid[0]) // coef, int(mid[1] // coef)), 5)  # Середина преобразованного отрезка

    # Соединяем середины
    for mid in midpoints:
        pygame.draw.line(screen, BLACK, (int(mid[0]) // coef, int(mid[1]) // coef),
                         (int(mid[0]) // coef, int(mid[1]) // coef), 3)

    pygame.display.flip()

# Завершение работы
pygame.quit()
