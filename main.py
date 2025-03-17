from window import *

def main():
    win = Window(800, 600)
    
    # Create and draw your test cells
    cell1 = Cell(win, 50, 50, 150, 150)
    cell1.draw()
    
    cell2 = Cell(win, 400, 450, 200, 200)
    cell2.draw()
    
    cell3 = Cell(win, 150,150, 420, 300)
    cell3.draw()
    
    cell1.draw_move(cell3)        # This should draw a red line from `cell1` to `cell2`
    cell3.draw_move(cell2, True)  # This should draw a gray line (undo) from `cell2` back to `cell1`
    
    win.wait_for_close()
    
if __name__ == '__main__':
    main()