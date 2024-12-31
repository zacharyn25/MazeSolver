from Cell import Cell
from time import sleep
import random 
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
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        if seed is not None: 
            random.seed(seed)
        self.create_cells()
        self.break_entrance_and_exit()
        self.break_walls_r(0, 0)
        self.reset_cells_visited()

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

    def draw_cell(self, i=None,j=None):
        if (i == None) or (j==None):
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    self._cells[i][j].draw("gray")
                    self.animate()
        else:
            self._cells[i][j].draw()
            self.animate()
    
    def animate(self):
        self.window.redraw()
        sleep(0.05)

    def break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        self.draw_cell(0,0)
        self.draw_cell(-1,-1)

    def break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            directions_list = []
            if (0 <= (i-1) < self.num_rows) and (0 <= j < self.num_cols):
                if not self._cells[i-1][j].visited:
                    directions_list.append((i-1,j))

            if (0 <= (i+1) < self.num_rows) and (0 <= j < self.num_cols):
                if not self._cells[i+1][j].visited:
                    directions_list.append((i+1,j))

            if (0 <= (i) < self.num_rows) and (0 <= (j-1) < self.num_cols):
                if not self._cells[i][j-1].visited:
                    directions_list.append((i, j-1))
            
            if (0 <= (i) < self.num_rows) and (0 <= (j+1) < self.num_cols):
                if not self._cells[i][j+1].visited:
                    directions_list.append((i, j+1))
                
            if directions_list == []:
                self.draw_cell(i,j)
                return
            
            index = random.randrange(len(directions_list))
            next_i, next_j = directions_list[index]

            # Break walls based on direction of movement
            if next_i < i:  # moving up
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][j].has_bottom_wall = False
            elif next_i > i:  # moving down
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][j].has_top_wall = False
            elif next_j < j:  # moving left
                self._cells[i][j].has_left_wall = False
                self._cells[i][next_j].has_right_wall = False
            else:  # moving right
                self._cells[i][j].has_right_wall = False
                self._cells[i][next_j].has_left_wall = False

            # Make recursive call to the new position
            self.break_walls_r(next_i, next_j)
    
    def reset_cells_visited(self):
        for i in range(self.num_rows):
                for j in range(self.num_cols):
                    self._cells[i][j].visited = False