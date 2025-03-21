from mechanics import *

#from maze import Maze

def main():
    #num_rows = 12
    #num_cols = 16
    #margin = 50
    screen_x = 800
    screen_y = 600
    #cell_size_x = (screen_x - 2 * margin) / num_cols
    #cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    
    # Create some points
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(300, 100)
    
    # Create lines
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p1)
    
    # Draw the lines
    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")
    win.draw_line(line3, "purple")

    #maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)

    
    win.wait_for_close()
    
if __name__ == '__main__':
    main()