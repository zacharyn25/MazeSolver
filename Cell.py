from Line import Line
from Point import Point
from tkinter import Tk, BOTH, Canvas

class Cell:
    def __init__(self,  x1,
                        x2,
                        y1,
                        y2,
                        window):
        self.has_left_wall = True
        self.has_right_wall =  True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.window = window

    def draw(self, fill_color="red"):
        if self.has_left_wall:
            point_1 = Point(self.x1,self.y1)
            point_2 = Point(self.x1,self.y2)
            line = Line(point_1, point_2)
            self.window.draw_line(line, fill_color)

        if self.has_right_wall:
            point_1 = Point(self.x2,self.y1)
            point_2 = Point(self.x2,self.y2)
            line = Line(point_1, point_2)
            self.window.draw_line(line, fill_color)

        if self.has_top_wall:
            point_1 = Point(self.x1,self.y1)
            point_2 = Point(self.x2,self.y1)
            line = Line(point_1, point_2)
            self.window.draw_line(line, fill_color)

        if self.has_bottom_wall:
            point_1 = Point(self.x1,self.y2)
            point_2 = Point(self.x2,self.y2)
            line = Line(point_1, point_2)
            self.window.draw_line(line, fill_color)

    def draw_move(self, to_cell, undo=False):
        cell_center = Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
        to_cell_center = Point((to_cell.x1 + to_cell.x2) / 2, (to_cell.y1 + to_cell.y2) / 2)
        line = Line(cell_center, to_cell_center)
        if undo:
            fill_color="gray"
        else:
            fill_color="red"
            
        self.window.draw_line(line, fill_color)
        