from window import *
import time
class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        
    def _create_cells(self):
        
        if self.num_rows <= 0 or self.num_cols <= 0:
            raise ValueError("Number of rows and columns must be greater than 0.")
        if self.cell_size_x <= 0 or self.cell_size_y <= 0:
            raise ValueError("Cell size must be greater than 0.")
        
        self._cells = []
        
        for row in range(self.num_rows):
            column = []
            for col in range(self.num_cols):
                 # Calculate x1, y1, x2, y2 for the cell
                cell_x1 = self.x1 + (col * self.cell_size_x)
                cell_y1 = self.y1 + (row * self.cell_size_y)
                cell_x2 = cell_x1 + self.cell_size_x
                cell_y2 = cell_y1 + self.cell_size_y

                # Create a Cell instance
                cell = Cell(self.win, cell_x1, cell_y1, cell_x2, cell_y2)

                # Add it to the row's list
                column.append(cell)
            self._cells.append(column)  # Add the row to the main cells list
    
    def _draw_cell(self, i, j):
        # Check if _cells has been initialized
        if not self._cells:
            raise ValueError("Cells have not been created yet, call _create_cells() first.")

        # Check bounds for i and j
        if i < 0 or i >= len(self._cells) or j < 0 or j >= len(self._cells[i]):
            raise IndexError(f"Cell index out of bounds: ({i}, {j})")
        
        cell = self._cells[i][j]  # Get the specific Cell object at coordinates (i, j)
        cell.draw()               # Use the Cell's draw method to render it
        self._animate()
        
    def _animate(self):
        self.win.redraw(self)
        time.sleep(0.07)