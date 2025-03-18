import unittest

from maze import *
from window import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells_different_dimensions(self):
        num_cols = 5
        num_rows = 8
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        # Verify outer and inner dimensions
        self.assertEqual(len(m1._cells), num_cols)  # Outer list should have `num_cols` entries
        self.assertEqual(len(m1._cells[0]), num_rows)  # Inner list for any column should have `num_rows` entries 
    
        
    def test_maze_cells_not_null(self):
        num_cols = 4
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Check that all cells in the grid are valid Cell instances
        for col in m1._cells:  # Outer loop iterates over each column
            for cell in col:  # Inner loop iterates over each cell in a column
                self.assertIsNotNone(cell)  # Ensure no cell is `None`
                self.assertIsInstance(cell, Cell)  # Ensure the cell is a valid `Cell` object
        
    
    def test_maze_invalid_dimensions(self):
        # Test invalid rows
        with self.assertRaises(ValueError):
            Maze(0, 0, 0, 5, 10, 10)  # Zero rows

        # Test invalid columns
        with self.assertRaises(ValueError):
            Maze(0, 0, 5, -3, 10, 10)  # Negative columns

        # Test invalid cell size
        with self.assertRaises(ValueError):
            Maze(0, 0, 5, 5, 0, 10)  # Zero cell width
        with self.assertRaises(ValueError):
            Maze(0, 0, 5, 5, 10, -15)  # Negative cell height
            
    def test_maze_grid_consistency(self):
        num_cols = 6
        num_rows = 4
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Verify that every column has exactly `num_rows` cells
        for col in m1._cells:
            self.assertEqual(len(col), num_rows)
            
    def test_maze_one_row_or_column(self):
        # Case: One row, many columns
        num_cols = 10
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(m1._cells), num_cols)  # Outer list corresponds to columns
        for col in m1._cells:
            self.assertEqual(len(col), num_rows)  # Each column has only one row

        # Case: Many rows, one column
        num_cols = 1
        num_rows = 10
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(m2._cells), num_cols)  # Outer list corresponds to columns
        for col in m2._cells:
            self.assertEqual(len(col), num_rows)  # This lone column has many rows
            
    def test_maze_empty_maze(self):
        with self.assertRaises(ValueError):  # Expect ValueError for invalid maze dimensions
            Maze(0, 0, 0, 0, 10, 10)  # Zero rows and columns

        with self.assertRaises(ValueError):
            Maze(0, 0, 0, 5, 10, 10)  # Zero rows is invalid

        with self.assertRaises(ValueError):
            Maze(0, 0, 5, 0, 10, 10)  # Zero columns is invalid
            
    
    def test_no_overlapping_cells(self):
        num_cols = 3
        num_rows = 3
        cell_size_x = 10
        cell_size_y = 10
        m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)

        # Collect all cell coordinates in a set for uniqueness
        coordinates = set()
        for col in m1._cells:
            for cell in col:
                coordinates.add((cell._x1, cell._y1, cell._x2, cell._y2))

        # The number of unique coordinates should equal the total number of cells
        self.assertEqual(len(coordinates), num_cols * num_rows)
        
    def test_large_maze(self):
        num_cols = 100
        num_rows = 100
        cell_size_x = 5
        cell_size_y = 5
        m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)

        # Assert the grid dimensions
        self.assertEqual(len(m1._cells), num_cols)
        for col in m1._cells:
            self.assertEqual(len(col), num_rows)
            
    def test_big_kahuna(self):
        num_cols = 20
        num_rows = 20
        cell_size_x = 5
        cell_size_y = 5
        m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)

        # 1. Validate grid dimensions
        self.assertEqual(len(m1._cells), num_cols)  # Correct number of columns
        for col in m1._cells:
            self.assertEqual(len(col), num_rows)  # Correct number of rows per column

        # 2. Check every cell in the maze has unique boundaries
        coordinates = set()  # To store cell boundaries
        for col in m1._cells:
            for cell in col:
                coordinates.add((cell._x1, cell._y1, cell._x2, cell._y2))  # Use correct attributes
        self.assertEqual(len(coordinates), num_cols * num_rows)  # Expect all cells to be unique

        # 3. Test cell adjacency (alignment with neighbors)
        for col_index, col in enumerate(m1._cells[:-1]):  # For all columns except the last
            for row_index, cell in enumerate(col[:-1]):  # For all rows except the last
                right_neighbor = m1._cells[col_index + 1][row_index]  # Cell to the right
                bottom_neighbor = m1._cells[col_index][row_index + 1]  # Cell below

                # Right neighbor's left edge should match this cell's right edge
                self.assertEqual(cell._x2, right_neighbor._x1)
                # Bottom neighbor's top edge should match this cell's bottom edge
                self.assertEqual(cell._y2, bottom_neighbor._y1)
    


class MockWindow(unittest.TestCase):
    def draw_line(self, line, color):
         pass  # Mock does nothing, simply satisfies the interface

    def test_break_entrance_and_exit(self):
        num_cols = 5
        num_rows = 5
        cell_size_x = 5
        cell_size_y = 5

        # Create a mock "window" object
        mock_window = MockWindow()

        # Pass the mock window to the Maze
        maze = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y, win=mock_window)

        # Reference the entrance and exit cells
        entrance = maze._cells[0][0]
        exit = maze._cells[-1][-1]

        # Assert initial state
        self.assertEqual(entrance.has_top_wall, True, "Entrance top wall should initially exist!")
        self.assertEqual(exit.has_bottom_wall, True, "Exit bottom wall should initially exist!")

        # Perform action
        maze._break_entrance_and_exit()

        # Validate changes
        self.assertEqual(entrance.has_top_wall, False, "Entrance top wall should be removed!")
        self.assertEqual(exit.has_bottom_wall, False, "Exit bottom wall should be removed!")
                   
            
if __name__ == "__main__":
    unittest.main()