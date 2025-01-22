import pygame
import math
from perlin_noise_algorithm import generate_perlin_noise

def run_perlin_noise():
    width, height = 500, 500
    scale = 10
    seed = 2
    height_map = generate_perlin_noise(width, height, scale, seed)
    print(height_map.min(), height_map.max())

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Perlin Noise Height Map')
    clock = pygame.time.Clock()

    def draw_height_map():
        for i in range(width):
            for j in range(height):
                value = height_map[j][i]
                if value < 120:
                    screen.set_at((i, j), (65, 105, 225))  # Niebieski
                elif value < 160:
                    screen.set_at((i, j), (238, 214, 175))  # Zolty
                elif value < 200:
                    screen.set_at((i, j), (34, 139, 34))  # Zielony
                elif value < 240:
                    screen.set_at((i, j), (139, 69, 19))  # Szary
                else:
                    screen.set_at((i, j), (255, 255, 255))  # Bialy

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #height_map = (height_map + 10) % 360
        draw_height_map()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def run_cloud_simulation():
    width, height = 800, 600
    big_width, big_height = 1600, 1200
    scale = 10
    seed = 42  

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    global cloud_surface
    cloud_surface = None  

    def generate_cloud_surface():
        global cloud_surface  
        if cloud_surface is None:
            noise = generate_perlin_noise(big_width, big_height, scale, seed=seed)
            cloud_surface = pygame.Surface((big_width, big_height), pygame.SRCALPHA)
            for y in range(big_height):
                for x in range(big_width):
                    value = int(max(0, min(255, noise[y, x]))) 
                    cloud_surface.set_at((x, y), (255, 255, 255, value))

    angle = 0
    radius = 150
    center_x, center_y = width // 2, height // 2

    generate_cloud_surface()

    running = True
    while running:
        screen.fill((135, 206, 235))
        offset_x = center_x + int(radius * math.cos(math.radians(angle)))
        offset_y = center_y + int(radius * math.sin(math.radians(angle)))
        screen.blit(cloud_surface, (0, 0), (offset_x, offset_y, width, height))

        angle += 0.3
        if angle >= 360:
            angle = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
