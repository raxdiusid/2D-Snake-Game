import pygame

import map
import snake

class Game:
    def __init__(self, WindowSize):
        self.Active = True
        self.Running = True
        self.WindowSize = WindowSize
        self.WindowWidth = WindowSize[0]
        self.WindowHeight = WindowSize[1]
        self.Screen = pygame.display.set_mode(WindowSize)

        self.Clock = pygame.time.Clock()
        self.t = 0

        self.Map = map.Map(self, [20, 20])
        self.Snake = snake.Snake(self, 0.1)

        self.add_game_attribute()
        self.game_render()

    def game_render(self):
        while self.Running:
            for Event in pygame.event.get():
                if Event.type == pygame.QUIT:
                    self.Running = False
                elif Event.type == pygame.KEYDOWN:
                    self.Snake.process_hotkey(Event.key)

            self.Screen.fill((0, 0, 0))
            self.Map.render_map()
            self.Snake.update_position()
            pygame.display.flip()
            self.t += self.Clock.tick(60)/1000
        pygame.quit()

    def add_game_attribute(self):
        pygame.display.set_caption("2D Pygame Snake")

    def game_reset(self):
        for i, j in enumerate(self.Snake.SnakePart):
            self.Snake.map_set(j[0], j[1], "grass")
        self.Snake.SnakePart = [[4, 10]]


game = Game((500, 500))