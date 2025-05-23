from graphics import Window
from cell import Cell
from maze import Maze
import sys

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    sys.setrecursionlimit(10000)

    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win,10)
    solvable = maze.solve()
    if not solvable:
        print("Maze can't be solved")
    else:
        print("Maze solved!")

    win.wait_for_close()
main()
