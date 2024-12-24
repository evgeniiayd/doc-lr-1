import pygame
import numpy as np

# Инициализация Pygame
pygame.init()

# Настройки окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Спираль улитки Паскаля')

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Параметры спирали
a = 100
b = 100
theta_max = 4 * np.pi  # Максимальный угол (4 витка)

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение фона
    screen.fill(WHITE)

    # Рисование спирали
    for i in range(1000):  # 1000 точек для рисования спирали
        theta = np.linspace(0, theta_max, 1000)[i]
        r = b + 2 * a * np.cos(theta)
        x = int((r * np.cos(theta) + width / 2))  # Смещение по X
        y = int((r * np.sin(theta) + height / 2))  # Смещение по Y

        # Рисуем точку на экране
        pygame.draw.circle(screen, BLUE, (x, y), 1)

    pygame.display.flip()

# Выход из Pygame
pygame.quit()
