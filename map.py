import random

import pygame


class Map:
    def __init__(self, Game, MapSize):
        self.Game = Game
        self.TileSize = MapSize
        self.TileWidth = MapSize[0]
        self.TileHeight = MapSize[1]
        self.MapTiles = self.load_map_tiles()
        
        self.generate_food()

    def load_map_tiles(self):
        MapTiles = []

        for i in range(self.TileHeight):
            MapTiles.append([])
            for j in range(self.TileWidth):
                MapTiles[i].append(0)

        return MapTiles
    
    def generate_food(self):
        MTN1 = len(self.MapTiles)-1
        x_food, y_food = random.randint(0, MTN1), random.randint(0, MTN1)
        food_cell = self.MapTiles[y_food][x_food]
        while food_cell == 2:
            x_food, y_food = random.randint(0, MTN1), random.randint(0, MTN1)
            food_cell = self.MapTiles[y_food][x_food]
        self.MapTiles[y_food][x_food] = 1

    def render_map(self):
        TileWidthSize = self.Game.WindowWidth / self.TileWidth
        TileHeightSize = self.Game.WindowHeight / self.TileHeight
        for i, arr_row in enumerate(self.MapTiles):
            for n, j in enumerate(arr_row):
                if j == 0:
                    pygame.draw.rect(
                        self.Game.Screen,
                        (0, 255, 0),
                        pygame.Rect(
                            n*TileWidthSize,
                            i*TileHeightSize,
                            TileWidthSize,
                            TileHeightSize
                        )
                    )
                elif j == 1:
                    pygame.draw.rect(
                        self.Game.Screen,
                        (255, 0, 0),
                        pygame.Rect(
                            n*TileWidthSize,
                            i*TileHeightSize,
                            TileWidthSize,
                            TileHeightSize
                        )
                    )
                elif j == 2:
                    pygame.draw.rect(
                        self.Game.Screen,
                        (255, 255, 255),
                        pygame.Rect(
                            n*TileWidthSize,
                            i*TileHeightSize,
                            TileWidthSize,
                            TileHeightSize
                        )
                    )