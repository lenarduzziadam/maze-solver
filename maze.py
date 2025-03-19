from window import *
import time
class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None,):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            random.seed(seed)
            
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        
    def _create_cells(self):
        
        if self.num_rows <= 0 or self.num_cols <= 0:
            raise ValueError("Number of rows and columns must be greater than 0.")
        if self.cell_size_x <= 0 or self.cell_size_y <= 0:
            raise ValueError("Cell size must be greater than 0.")
        
        self._cells = []
        
        for col in range(self.num_cols):  # Outer loop is now for columns
            column = []
            for row in range(self.num_rows):  # Inner loop is for rows
                # Calculate x1, y1, x2, y2 for the cell
                cell_x1 = self.x1 + (col * self.cell_size_x)
                cell_y1 = self.y1 + (row * self.cell_size_y)
                cell_x2 = cell_x1 + self.cell_size_x
                cell_y2 = cell_y1 + self.cell_size_y

                # Create a Cell instance
                cell = Cell(self.win, cell_x1, cell_y1, cell_x2, cell_y2)

                # Add the cell to the column list
                column.append(cell)
            self._cells.append(column)  # Add the column to the main list
    
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
        self.win.redraw()
        time.sleep(0.07)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
        
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
            