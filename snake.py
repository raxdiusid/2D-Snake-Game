import pygame

class Snake:
    def __init__(self, Game, dt):
        self.Game = Game
        
        self.dt = dt
        self.next_t = self.dt
        
        self.SnakePart = [[4, 10]]

        self.Hotkey = "up"

    def update_position(self):
        for snake_part in self.SnakePart:
            self.map_set(snake_part[0], snake_part[1], "snake")

        if pygame.time.get_ticks()/1000 < self.next_t:
            return
        
        self.sp_copy = self.sp_deep_copy()

        if self.Hotkey == "up":
            self.SnakePart[0][1] -= 1
        elif self.Hotkey == "down":
            self.SnakePart[0][1] += 1
        elif self.Hotkey == "right":
            self.SnakePart[0][0] += 1
        elif self.Hotkey == "left":
            self.SnakePart[0][0] -= 1

        for j in range(1, len(self.SnakePart)):
            self.SnakePart[j] = self.sp_copy[j-1]

        if self.SnakePart[0][0] < 0:
            self.SnakePart[0][0] = self.Game.Map.TileWidth-1
        if self.SnakePart[0][0] > self.Game.Map.TileWidth-1:
            self.SnakePart[0][0] = 0
        if self.SnakePart[0][1] < 0:
            self.SnakePart[0][1] = self.Game.Map.TileHeight-1
        if self.SnakePart[0][1] > self.Game.Map.TileHeight-1:
            self.SnakePart[0][1] = 0

        next_cell = self.Game.Map.MapTiles[self.SnakePart[0][1]][self.SnakePart[0][0]]
        if next_cell == 1:
            self.add_tail()
            self.Game.Map.generate_food()
        elif next_cell == 2:
            self.Game.game_reset()

        self.map_set(self.sp_copy[-1][0], self.sp_copy[-1][1], "grass")

        self.next_t += self.dt

    def add_tail(self):
        self.SnakePart.append(self.sp_copy[-1])

    def process_hotkey(self, key):
        if key == pygame.K_w:
            if self.Hotkey == "down":
                return
            self.Hotkey = "up"
        elif key == pygame.K_s:
            if self.Hotkey == "up":
                return
            self.Hotkey = "down"
        elif key == pygame.K_a:
            if self.Hotkey == "right":
                return
            self.Hotkey = "left"
        elif key == pygame.K_d:
            if self.Hotkey == "left":
                return
            self.Hotkey = "right"

    def map_set(self, x, y, mode):
        if mode == "food":
            self.Game.Map.MapTiles[y][x] = 1
        elif mode == "grass":
            self.Game.Map.MapTiles[y][x] = 0
        elif mode == "snake":
            self.Game.Map.MapTiles[y][x] = 2

    def sp_deep_copy(self):
        t = []
        for j in self.SnakePart:
            t.append([j[0], j[1]])
        return t
