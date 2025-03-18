from tkinter import Tk, BOTH, Canvas
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
        
    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width=2)
class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        #creating root widget
        self.__root = Tk()
        #set root widget title
        self.__root.title('Maze Solver')
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
        #create canvas with root keeping width and height as parameters
        self.__canvas = Canvas(self.__root, width=width, height=height)
        #packs canvas to prepare for drawing
        self.__canvas.pack(fill=BOTH, expand=1)
        
        #creates running variable setting it to false
        self.running = False
        
        
    
    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()
        
    def wait_for_close(self):
        #sets self.running to true then iterates through loop until running is no longer true
        self.running = True
        while self.running:
            self.redraw()
            
    def close(self):
        self.running = False
    
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)
        
        
class Cell:
    def __init__(self, win, x1, y1, x2, y2, has_left_wall=True, 
             has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        
        self._win = win
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall  
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        
        self.visited = False
        
    def draw(self):
        #if statments to check and draw walls if needed
        if self.has_left_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")
            
        if self.has_top_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x2, self._y1)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")
            
        if self.has_bottom_wall:
            p1 = Point(self._x1, self._y2)
            p2 = Point(self._x2, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            p1 = Point(self._x2, self._y1)
            p2 = Point(self._x2, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")
    
    def draw_move(self, to_cell, undo=False):
        self.to_cell = to_cell
        self.undo = undo
        
        center_x = (self._x1 + self._x2) / 2
        center_y = (self._y1 + self._y2) / 2
        
        other_center_x = (to_cell._x1 + to_cell._x2) / 2
        other_center_y = (to_cell._y1 + to_cell._y2) / 2
        
        if undo:
            fill_line = "gray"
        else:
            fill_line = "red"
        
        self_point = Point(center_x, center_y)
        other_point = Point(other_center_x, other_center_y)
        line = Line(self_point, other_point)
        self._win.draw_line(line, fill_line)
        


    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
            
        while True:
            possible_directions = []
            
            # Check north (i-1, j)
            if i > 0 and not self._cells[i-1][j].visited:
                possible_directions.append((i-1, j, "north"))
                
            # Check south (i+1, j)
            if i < self._num_rows-1 and not self._cells[i+1][j].visited:
                possible_directions.append((i+1, j, "south"))
                
            # Check west (i, j-1)
            if j > 0 and not self._cells[i][j-1].visited:
                possible_directions.append((i, j-1, "west"))
                
            # Check east (i, j+1)
            if j < self._num_cols-1 and not self._cells[i][j+1].visited:
                possible_directions.append((i, j+1, "east"))
            
            # If there are no possible directions, draw and return
            if len(possible_directions) == 0:
                current_cell.draw()  # You might already have a draw method
                return

            
            # Pick a random direction
            next_i, next_j, direction = random.choice(possible_directions)
    
            # Break down the wall between current cell and chosen cell
            if direction == "north":
                current_cell.has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            elif direction == "south":
                current_cell.has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            elif direction == "west":
                current_cell.has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
                
            elif direction == "east":
                current_cell.has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
                
            # Recursively call the method on the next cell
            self._break_walls_r(next_i, next_j)