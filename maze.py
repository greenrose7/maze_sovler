from graphics import Cell, Point
from time import sleep
from random import randint

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        self._break_enterance_and_exit()
    
    def _create_cells(self):
        top_left_point = Point(self.x1, self.y1)
        #bottom_right_point = Point(self.x1 + self.cell_size_x, self.y1 + self.cell_size_y)
        for x in range(self.num_cols):
            col = []
            for y in range(self.num_rows):
                cell = Cell(top_left_point, Point(top_left_point.x + self.cell_size_x, top_left_point.y + self.cell_size_y), self.win)
                col.append(cell)
                cell.draw()
                self._animate()
                top_left_point = Point(top_left_point.x, top_left_point.y + self.cell_size_y)
            self._cells.append(col)
            # top_left_point.y = self.y1
            # top_left_point.x += self.cell_size_x
            top_left_point = Point(top_left_point.x + self.cell_size_x, self.y1)
    
    def _animate(self):
        if self.win == None:
            return
        self.win.redraw()
        sleep(0.05)
    
    def _break_enterance_and_exit(self):
        ## Entrance (top left cell)
        match randint(0,1):
            case 0:
                self._cells[0][0].has_left_wall = False
            case 1:
                self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        ## Exit (bottom right cell)
        match randint(0,1):
            case 0:
                self._cells[self.num_cols-1][self.num_rows-1].has_right_wall = False
            case 1:
                self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._cells[self.num_cols-1][self.num_rows-1].draw()
