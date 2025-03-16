from window import *

def main():
    win = Window(800, 600)
    
     # Create some points
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(300, 100)
    p4 = Point(420, 150)
    # Create lines using those points
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p1)
    line4 = Line(p1, p4)
    
    # Draw the lines with different colors
    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")
    win.draw_line(line3, "green")
    win.draw_line(line4, "yellow")
    
    win.wait_for_close()
    
if __name__ == '__main__':
    main()