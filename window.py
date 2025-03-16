from tkinter import Tk, BOTH, Canvas
import tkinter as tk

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
    def __init__(self, has_left_wall=True,
                    has_right_wall=True,
                    has_top_wall=True,
                    has_bottom_wall=True, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
    def draw(self):
        
        
        
    
