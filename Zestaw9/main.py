import sys
import pygame
import random

# Kolory
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)


# Klasa reprezentująca płatki śniegu (Block)
class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y, speed):
        super().__init__()
        self.image = pygame.Surface([50, 60])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        global snow_heap_height
        if self.rect.bottom + snow_heap_height > height:
            snow_heap_height += 10
            self.kill()


# Inicjalizacja Pygame
pygame.init()
size = (width, height) = (800, 600)
screen = pygame.display.set_mode()
pygame.display.set_caption('Falling Snow')

# Ustawienia gry
FPS = 60
clock = pygame.time.Clock()

sprite_group = pygame.sprite.Group()
snowflake_speed = 1

# Dodawanie płatków śniegu
ADD_SNOWFLAKE = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_SNOWFLAKE, 600)

# Zmienne zaspy
snow_heap_height = 0
max_heap_height = height

# Licznik
font = pygame.font.Font(None, 40)
counter = 0

# Czas gry
game_time = 0

# Pętla gry
while True:
    dt = clock.tick(60)
    game_time += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in sprite_group:
                if sprite.rect.collidepoint(event.pos):
                    sprite_group.remove(sprite)
                    counter += 1

        elif event.type == ADD_SNOWFLAKE:
            collision = True
            while collision:
                x = random.randint(0, width - 10)
                snowflake = Block(white, x, 0, snowflake_speed)
                collision = pygame.sprite.spritecollideany(snowflake, sprite_group)
            sprite_group.add(snowflake)

    # Zmiana szybkości
    if game_time // 10000 > 0:
        snowflake_speed += 1
        game_time %= 10000

    # Warunek końca gry
    if snow_heap_height >= max_heap_height:
        text = "Przegrałeś! Zaspa zajęła cały ekran."
        text_surf = font.render(text, True, blue)
        text_rect = text_surf.get_rect(center=(width // 2, height // 2))
        screen.blit(text_surf, text_rect)
        pygame.display.flip()
        pygame.time.delay(5000)
        pygame.quit()
        sys.exit(0)

    # Rysowanie ekranu
    sprite_group.update()
    screen.fill(black)
    sprite_group.draw(screen)

    # Wyświetlanie licznika
    counter_text = font.render(f"Counter: {counter}", True, blue)
    screen.blit(counter_text, (10, 10))
    pygame.draw.rect(screen, white, (0, height - snow_heap_height, width, snow_heap_height))

    pygame.display.flip()
    clock.tick(FPS)


