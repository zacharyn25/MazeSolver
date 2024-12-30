from Window import Window
from Point import Point
from Line import Line
from Cell import Cell
from Maze import Maze

def main():
    win = Window(800, 600)
    point_1 = Point(0,0)
    point_2 = Point(800,600)
    line = Line(point_1, point_2)
    cell = Cell(0, 50, 0, 40,win)
    cell_2 = Cell(200, 280, 200, 396,win)
    cell.draw()
    cell_2.draw()
    cell.draw_move(cell_2, True)

    maze = Maze(0,0,50,50,10,10,win)

    win.wait_for_close()

if __name__ == "__main__":
    main()