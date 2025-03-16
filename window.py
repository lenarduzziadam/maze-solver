from tkinter import Tk, BOTH, Canvas
import tkinter as tk

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        #creating root widget
        self.__root = Tk()
        #set root widget title
        self.__root.title('Maze Solver')
        
        #create canvas with root keeping width and height as parameters
        self.__canvas = Canvas(self.__root, width=width, height=height)
        #packs canvas to prepare for drawing
        self.__canvas.pack(fill=BOTH, expand=1)
        
        #creates running variable setting it to false
        self.running = False
        
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
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