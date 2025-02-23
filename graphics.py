from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height, title :str):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title(title)
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack()
        self.running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
    
    def draw_line(self, line, fill_color :str):
        line.draw(self.canvas, fill_color)

class Point():
    def __init__(self, x :int, y :int):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if type(other) is not Point:
            raise ValueError("Adding non-point to point")
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
    
    def __truediv__(self, divisor):
        if type(divisor) is not int and type(divisor) is not float:
            raise ValueError("Must divide point by number")
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        return Point(self.x/divisor, self.y/divisor)

class Line():
    def __init__(self, point_one :Point, point_two :Point):
        self.point_one = point_one
        self.point_two = point_two

    def draw(self, canvas :Canvas, fill_color :str):
        canvas.create_line(self.point_one.x, self.point_one.y, self.point_two.x, self.point_two.y, fill=fill_color, width=2)

class Cell():
    def __init__(self, tl_point :Point, br_point :Point, window :Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        # self._x1 = tl_point.x
        # self._y1 = tl_point.y
        # self._x2 = br_point.x
        # self._y2 = br_point.y
        self._tl_point = tl_point
        self._br_point = br_point
        self.window = window
    
    def draw(self):
        if self.window == None:
            #print("No Window; skipping draw")
            return
        tr_point = Point(self._br_point.x, self._tl_point.y)
        bl_point = Point(self._tl_point.x, self._br_point.y)
        if self.has_bottom_wall:
            line = Line(bl_point, self._br_point)
            line.draw(self.window.canvas, "black")
        if self.has_top_wall:
            line = Line(tr_point, self._tl_point)
            line.draw(self.window.canvas, "black")
        if self.has_left_wall:
            line = Line(bl_point, self._tl_point)
            line.draw(self.window.canvas, "black")
        if self.has_right_wall:
            line = Line(tr_point, self._br_point)
            line.draw(self.window.canvas, "black")
    
    def draw_move(self, to_cell, undo=False):
        start = (self._tl_point + self._br_point) / 2
        end = (to_cell._tl_point + to_cell._br_point) / 2
        line = Line(start, end)
        color = "red"
        if undo:
            color = "gray"
        line.draw(self.window.canvas, color)