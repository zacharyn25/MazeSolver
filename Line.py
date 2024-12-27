from Point import Point
from tkinter import Tk, BOTH, Canvas
class Line:
    def __init__(self, point_1: Point , point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width=2)