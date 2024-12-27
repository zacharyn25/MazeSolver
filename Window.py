from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width 
        self.height = height
        self.root_widget = Tk()
        self.root_widget.title("Maze")
        self.canvas_widget = Canvas(self.root_widget, height=self.height, width=self.width)
        self.canvas_widget.pack(fill=BOTH)
        self.window_running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.window_running = True
        while(self.window_running):
            self.redraw()

    def close(self):
        self.window_running = False
