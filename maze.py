from graphics import Cell, Point
from time import sleep
from random import randint, seed

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
        maze_seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if maze_seed != None:
            seed(maze_seed)
        else:
            seed(0)
        self._cells = []
        self._create_cells()
        self._break_enterance_and_exit()
        self._break_walls_r(0,0)
        self._reset_visited_cells()
    
    def _create_cells(self):
        top_left_point = Point(self.x1, self.y1)
        #bottom_right_point = Point(self.x1 + self.cell_size_x, self.y1 + self.cell_size_y)
        for x in range(self.num_cols):
            col = []
            for y in range(self.num_rows):
                cell = Cell(top_left_point, Point(top_left_point.x + self.cell_size_x, top_left_point.y + self.cell_size_y), self.win)
                col.append(cell)
                cell.draw()
                self._animate(0.02)
                top_left_point = Point(top_left_point.x, top_left_point.y + self.cell_size_y)
            self._cells.append(col)
            # top_left_point.y = self.y1
            # top_left_point.x += self.cell_size_x
            top_left_point = Point(top_left_point.x + self.cell_size_x, self.y1)
    
    def _animate(self, speed=0.05):
        if self.win == None:
            return
        self.win.redraw()
        sleep(speed)
    
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
    
    def _break_walls_r(self, current_x, current_y):
        self._cells[current_x][current_y].visited = True
        while True:
            to_visit = []
            current_neighbors = self._find_adjacent_cells(current_x, current_y)
            if len(current_neighbors) < 1:
                self._cells[current_x][current_y].draw()
                self._animate(0.04)
                return
            to_visit.extend(current_neighbors)
            #print(f"Neighbors: {current_neighbors}")
            random_adjacent_cell = current_neighbors[randint(0, len(current_neighbors)-1)]
            adjacent_x, adjacent_y = random_adjacent_cell
            if current_x < adjacent_x:
                self._cells[current_x][current_y].has_right_wall = False
                self._cells[adjacent_x][adjacent_y].has_left_wall = False
            elif current_x > adjacent_x:
                self._cells[current_x][current_y].has_left_wall = False
                self._cells[adjacent_x][adjacent_y].has_right_wall = False
            elif current_y < adjacent_y:
                self._cells[current_x][current_y].has_bottom_wall = False
                self._cells[adjacent_x][adjacent_y].has_top_wall = False
            elif current_y > adjacent_y:
                self._cells[current_x][current_y].has_top_wall = False
                self._cells[adjacent_x][adjacent_y].has_bottom_wall = False
            self._break_walls_r(adjacent_x, adjacent_y)
    
    def _find_adjacent_cells(self, x, y): #Finds adjacent unvisited cells (as tuples)
        adjacent_cells = []
        if x-1 >= 0:
            if self._cells[x-1][y].visited == False:
                adjacent_cells.append((x-1, y))
        if x+1 < self.num_cols:
            if self._cells[x+1][y].visited == False:
                adjacent_cells.append((x+1, y))
        if y-1 >= 0:
            if self._cells[x][y-1].visited == False:
                adjacent_cells.append((x, y-1))
        if y+1 < self.num_rows:
            if self._cells[x][y+1].visited == False:
                adjacent_cells.append((x, y+1))
        #print(adjacent_cells)
        return adjacent_cells

    def _reset_visited_cells(self):
        for i in self._cells:
            for j in i:
                j.visited = False