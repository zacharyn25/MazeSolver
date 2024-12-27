from Window import Window
from Point import Point
from Line import Line

def main():
    win = Window(800, 600)
    point_1 = Point(0,0)
    point_2 = Point(800,600)
    line = Line(point_1, point_2)
    win.draw_line(line, "red")
    win.wait_for_close()

if __name__ == "__main__":
    main()