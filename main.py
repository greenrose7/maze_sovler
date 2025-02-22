from graphics import *

def main():
    win = Window(800, 600, "my title")
    test_lines(win)
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

if __name__ == "__main__":
    main()