from graphics import Cell, Point
from time import sleep

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
        self._create_cells()
    
    def _create_cells(self):
        self._cells = []
        top_left_point = Point(self.x1, self.y1)
        #bottom_right_point = Point(self.x1 + self.cell_size_x, self.y1 + self.cell_size_y)
        for x in range(self.num_cols):
            col = []
            for y in range(self.num_rows):
                cell = Cell(top_left_point, Point(top_left_point.x + self.cell_size_x, top_left_point.y + self.cell_size_y), self.win)
                col.append(cell)
                cell.draw()
                self._animate()
                top_left_point.y += self.cell_size_y
            self._cells.append(col)
            top_left_point.y = self.y1
            top_left_point.x += self.cell_size_x
    
    def _animate(self):
        if self.win == None:
            return
        self.win.redraw()
        sleep(0.05)