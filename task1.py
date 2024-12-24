import pygame
import numpy as np

# Определяем размеры окна
WIDTH, HEIGHT = 600, 600
coef = 25

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Transformation")

# Определяем цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# Функция для отображения текста
def draw_text(text, x, y):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (x, y))


# Основная программа
# Очистка экрана
screen.fill(WHITE)

# Ввод координат точки
try:
    x = float(input("Введите координату x: "))
    y = float(input("Введите координату y: "))
except ValueError:
    print("Пожалуйста, введите корректные числа.")

# Исходные координаты
original_point = np.array([[x], [y]])

# Матрица преобразования
T = np.array([[1, 3],
             [4, 1]])

# Применение матричного преобразования
transformed_point = T @ original_point

# Вывод на экран
print(f"Исходные координаты: ({x}, {y})")
print(f"Преобразованные координаты: ({transformed_point[0, 0]}, {transformed_point[1, 0]})")

# Рисуем точки
pygame.draw.circle(screen, RED, (int(x * coef + WIDTH // 2), HEIGHT - int(y * coef + HEIGHT // 2)), 5)
pygame.draw.circle(screen, BLUE, (int(transformed_point[0, 0] * coef + WIDTH // 2),
                                  HEIGHT - int(transformed_point[1, 0] * coef + HEIGHT // 2)), 5)


# Обновление экрана
pygame.display.flip()

# Задержка перед следующим вводом
pygame.time.delay(10000)

