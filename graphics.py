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

class Line():
    def __init__(self, point_one :Point, point_two :Point):
        self.point_one = point_one
        self.point_two = point_two

    def draw(self, canvas :Canvas, fill_color :str):
        canvas.create_line(self.point_one.x, self.point_one.y, self.point_two.x, self.point_two.y, fill=fill_color, width=2)
