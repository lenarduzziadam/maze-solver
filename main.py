from window import *

def main():
    win = Window(800, 600)
    
    # Create and draw your test cells
    cell1 = Cell(win, 50, 50, 150, 150, has_left_wall=False)
    cell1.draw()
    
    cell2 = Cell(win, 200, 200, 300, 150, has_right_wall=False)
    cell2.draw()
    
    cell3 = Cell(win, 75,100, 200, 300)
    cell3.draw()
    
    win.wait_for_close()
    
if __name__ == '__main__':
    main()