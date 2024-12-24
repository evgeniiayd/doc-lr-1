import pygame
import sys

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Графические примитивы в Pygame")

# Определяем цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполняем экран белым цветом
    screen.fill(WHITE)

    # Рисуем окружность
    pygame.draw.circle(screen, RED, (400, 300), 100)

    # Рисуем линии
    pygame.draw.line(screen, GREEN, (100, 100), (700, 100), 5)
    pygame.draw.line(screen, BLUE, (100, 200), (700, 200), 5)

    # Рисуем текст
    font = pygame.font.Font(None, 74)
    text = font.render("Привет, мир!", True, YELLOW)
    screen.blit(text, (200, 400))

    # Обновляем экран
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()
