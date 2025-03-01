from graphics import *
from maze import Maze
from time import sleep
from random import random

def main():
    win = Window(800, 600, "my title")
    # test_lines(win)
    # cell1, cell2, cell3 = test_cells(win)
    # test_move_draw(cell1, cell2, cell3)
    # test_move_draw(cell1, cell2, cell3, undo=True)
    maze = Maze(30, 30, 11, 15, 50, 50, win, random())
    maze.solve()
    win.wait_for_close()

def test_lines(window :Window):
    top_left = Point(0,0)
    bottom_right = Point(800, 600)
    tl_br_line = Line(top_left, bottom_right)
    tl_br_line.draw(window.canvas, "red")

    mid_left = Point(0, 300)
    mid_right = Point(800, 300)
    ml_mr_line = Line(mid_right, mid_left)
    ml_mr_line.draw(window.canvas, "purple")

def test_cells(window :Window):
    cell_1 = Cell(Point(10, 10), Point(30, 30), window)
    cell_1.draw()
    cell_2 = Cell(Point(30, 30), Point(80, 80), window)
    cell_2.has_bottom_wall = False
    cell_2.has_right_wall = False
    cell_2.draw()
    
    cell_3 = Cell(Point(100, 100), Point(200, 150), window)
    cell_3.has_top_wall = False
    cell_3.draw()
    return cell_1, cell_2, cell_3

def test_move_draw(*args, undo=False):
    if len(args) < 2:
        print("Not enough cells to draw between")
        return
    last_point :Cell = None 
    cell :Cell
    for cell in args:
        if last_point != None:
            last_point.draw_move(cell, undo)
        last_point = cell



if __name__ == "__main__":
    main()