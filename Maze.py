from Cell import Cell
from time import sleep
class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.create_cells()

    def create_cells(self):
        self._cells = []  # Start with an empty list for the grid

        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                x1 = self.x1 + j * self.cell_size_x
                y1 = self.y1 + i * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                row.append(Cell(x1, x2, y1, y2, self.window))  
            self._cells.append(row)
        self.draw_cell()

    def draw_cell(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].draw("gray")
                self.animate()
    
    def animate(self):
        self.window.redraw()
        sleep(0.05)
