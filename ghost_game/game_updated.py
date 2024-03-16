import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Определение констант
WIDTH, HEIGHT = 800, 600
FPS = 30

# Определение цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (100, 100, 100)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Haunted House Adventure")

# Переменные для хранения состояния игры
feeling_brave = True
door_with_ghost = random.randint(1, 3)
doors_passed = 0

# Основной цикл игры
clock = pygame.time.Clock()

while feeling_brave:
    screen.fill(WHITE)

    # Отрисовка дверей
    for i in range(3):
        pygame.draw.rect(screen, GRAY, (i * WIDTH // 3, HEIGHT // 2 - 50, 100, 100))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            chosen_door = (
                mouse_x // (WIDTH // 3) + 1
            )  # Определение, на какую дверь нажали

            if chosen_door == door_with_ghost:
                feeling_brave = False
            else:
                doors_passed += 1

    # Отображение количества пройденных дверей
    font = pygame.font.Font(None, 36)
    text = font.render(f"Doors passed: {doors_passed}", True, RED)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

# Если привидение было найдено
screen.fill(WHITE)
pygame.draw.rect(screen, RED, (WIDTH // 2 - 50, HEIGHT // 2 - 50, 100, 100))
pygame.display.flip()

# Ждем 2 секунды перед выходом
pygame.time.wait(2000)
pygame.quit()
sys.exit()
