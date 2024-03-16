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

# Определение переменных
doors_passed = 0


def main_menu():
    global doors_passed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        print_text("Главное Меню", 40, WIDTH // 2, HEIGHT // 4)
        print_text(
            f"Ваш последний счёт: {doors_passed} двери/дверей",
            30,
            WIDTH // 2,
            HEIGHT // 2,
        )

        button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
        pygame.draw.rect(screen, GRAY, button_rect)
        print_text("1. Начать", 30, WIDTH // 2, HEIGHT // 2 + 75)

        pygame.display.flip()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_x, mouse_y):
            if pygame.mouse.get_pressed()[0]:
                doors_passed = explore_house()


def explore_house():
    global doors_passed
    feeling_brave = True
    lives = 3
    ghost_door = random.randint(1, 3)
    print("Добро пожаловать в дом с привидениями!")

    while feeling_brave and lives > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        print_text(
            "Перед вами 3 двери. Нужно выбрать одну.", 30, WIDTH // 2, HEIGHT // 4
        )

        doors_rects = [
            pygame.Rect(i * WIDTH // 3, HEIGHT // 2 - 50, 100, 100) for i in range(3)
        ]
        for rect in doors_rects:
            pygame.draw.rect(screen, GRAY, rect)

        # Отображение количества жизней в правом верхнем углу
        print_text(f"Жизни: {lives}", 20, WIDTH - 100, 20)

        pygame.display.flip()

        chosen_door = None
        while chosen_door is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for i, rect in enumerate(doors_rects):
                        if rect.collidepoint(mouse_x, mouse_y):
                            chosen_door = i + 1
                            break

        if chosen_door == ghost_door:
            if lives > 0:
                print("\nНеверная дверь!")
                print_text(
                    "Вы открыли дверь и увидели привидение! Ваша храбрость исчезает.",
                    25,
                    WIDTH // 2,
                    HEIGHT // 2,
                )
                print_text(
                    f"Осталось жизней: {lives}", 25, WIDTH // 2, HEIGHT // 2 + 50
                )
                lives -= 1
                pygame.display.flip()
                pygame.time.wait(2000)
        else:
            print(
                "\nВы спокойно проходите через дверь. Загибаете пальцы, подсчитывая, сколько дверей вы прошли."
            )
            doors_passed += 1
            pygame.display.flip()
            pygame.time.wait(2000)

    print("\nВаша храбрость испаряется. Вы бежите из этого дома, не оглядываясь.")
    print_text(f"Вы прошли {doors_passed} дверей.", 25, WIDTH // 2, HEIGHT // 2 + 50)
    pygame.display.flip()
    pygame.time.wait(2000)
    return doors_passed


def print_text(text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, RED)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def main():
    main_menu()


if __name__ == "__main__":
    main()
