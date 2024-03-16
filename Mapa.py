import os
import pygame
import random

TILE_SIZE = 64
MAP_SIZE = 13


class Mapa(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite_dir = os.path.join('assets', 'sprites')
        self.tile_mappings = {
            0: pygame.image.load(os.path.join(self.sprite_dir, "border.png")).convert_alpha(),
            1: pygame.image.load(os.path.join(self.sprite_dir, "ground.png")).convert_alpha(),
            2: pygame.image.load(os.path.join(self.sprite_dir, "spawn.png")).convert_alpha(),
             3: pygame.image.load(os.path.join(self.sprite_dir, "lava.png")).convert_alpha(),
            4: pygame.image.load(os.path.join(self.sprite_dir, "sand.png")).convert_alpha()
        }

        self.tile_mappings = {key: pygame.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))
                              for key, image in self.tile_mappings.items()}
        self.mapa = [
            [0] * 13,
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0] * 13
        ]

        self.generate_lava()
        self.generate_sand()

    def generate_lava(self):
        # Definir un área para el lago de lava
        lake_size = 4
        lake_center = (random.randint(lake_size // 2, MAP_SIZE - lake_size // 2 - 1),
                       random.randint(lake_size // 2, MAP_SIZE - lake_size // 2 - 1))

        # Generar el lago de lava adyacente
        for y in range(1, MAP_SIZE - 1):
            for x in range(1, MAP_SIZE - 1):
                dx = x - lake_center[0]
                dy = y - lake_center[1]
                if abs(dx) <= lake_size // 2 and abs(dy) <= lake_size // 2:
                    if random.random() < 0.5:
                        self.mapa[y][x] = 3

    def generate_sand(self):
        # Definir un área para el lago de lava
        lake_size = 4
        lake_center = (random.randint(lake_size // 2, MAP_SIZE - lake_size // 2 - 1),
                       random.randint(lake_size // 2, MAP_SIZE - lake_size // 2 - 1))

        # Generar el lago de lava adyacente
        for y in range(1, MAP_SIZE - 1):
            for x in range(1, MAP_SIZE - 1):
                dx = x - lake_center[0]
                dy = y - lake_center[1]
                if abs(dx) <= lake_size // 2 and abs(dy) <= lake_size // 2:
                    if random.random() < 0.5:
                        self.mapa[y][x] = 4

    def draw(self, screen):
        for row_index, row in enumerate(self.mapa):
            for col_index, tile_type in enumerate(row):
                tile = self.tile_mappings.get(tile_type)
                if tile:
                    screen.blit(tile, (col_index * TILE_SIZE, row_index * TILE_SIZE))

    @property
    def tile_costs(self):
        return {
            0: float('inf'),  # Costo infinito para los bordes
            1: 1,  # Costo bajo para el suelo
            2: 1,  # Costo bajo para el punto de inicio
            3: 10,  # Costo alto para la lava
            4: 2  # Costo moderado para la arena
        }
