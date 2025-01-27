# 2D-Snake-Game
2D snake game using Pygame

How this game works:
A multidimensional array is created to map all the tiles. We begin making symbol for each tile, where:
0 : Grass tile (Green color)
1 : Food tile (Red color)
2 : Snake part tile (White color)

For snake's movement, snake_part[j] will occupy snake_part[j-1] position.
