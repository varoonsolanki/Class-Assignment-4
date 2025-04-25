import tkinter as tk

# Constants for the canvas dimensions and grid size
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserCanvas:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        # Create a grid of blue cells
        self.cells = []
        for row in range(CANVAS_HEIGHT // CELL_SIZE):
            for col in range(CANVAS_WIDTH // CELL_SIZE):
                left_x = col * CELL_SIZE
                top_y = row * CELL_SIZE
                right_x = left_x + CELL_SIZE
                bottom_y = top_y + CELL_SIZE
                cell = self.canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="blue")
                self.cells.append(cell)

        # Create the eraser rectangle (pink color)
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")

        # Bind mouse movement to update the eraser's position
        self.canvas.bind("<Motion>", self.move_eraser)

    def move_eraser(self, event):
        # Get the current mouse position
        mouse_x = event.x
        mouse_y = event.y

        # Move the eraser rectangle to the mouse position
        self.canvas.coords(self.eraser, mouse_x, mouse_y, mouse_x + ERASER_SIZE, mouse_y + ERASER_SIZE)

        # Erase the cells in contact with the eraser
        self.erase_cells(mouse_x, mouse_y)

    def erase_cells(self, mouse_x, mouse_y):
        # Find all the cells that overlap with the eraser
        for cell in self.cells:
            coords = self.canvas.coords(cell)
            cell_left_x, cell_top_y, cell_right_x, cell_bottom_y = coords
            if (mouse_x + ERASER_SIZE > cell_left_x and mouse_x < cell_right_x) and \
               (mouse_y + ERASER_SIZE > cell_top_y and mouse_y < cell_bottom_y):
                # Change the cell color to white (erase it)
                self.canvas.itemconfig(cell, fill="white")

# Create the Tkinter window
root = tk.Tk()
root.title("Canvas Eraser")

# Create the EraserCanvas
eraser_canvas = EraserCanvas(root)

# Run the Tkinter event loop
root.mainloop()
