from tkinter import *
import settings 
import utils
from cell import Cell
##################   Game GUI creation     ###############
root = Tk()  
# ovverdiding the window settings 
root.configure(bg='black')                              #background color
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')    #window size 
root.title("Minesweaper Game")                          #window title 
root.resizable(False,False)                             #no window resize 


#Frame creation 
top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0,y=0)

game_title = Label (
    top_frame,
    bg = 'Black',
    fg = 'White',
    text= 'MineSweeper Game',
    font = ('',48)
)
game_title.place(
    x = utils.width_prct(25), y =0
)


left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height= utils.height_prct(75)
)
left_frame.place(x=0,y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg = 'black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

## button with out the cell class 
# btn1 = Button(
#     center_frame,               # have to give him the frame to be placed in it later according to wanted position
#     bg='blue',
#     text= = 'first button'
# )
# btn1.place(x=0,y=0)

##### note ======>>>>  btn.place wont be used as its hard coding  

## Button creation using CELL class ## 
for x in range(settings.GRID_SIZE):
    for y in range (settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column = x, row = y 
        )

# call the label from the cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x =0 , y= 0
)
#print(Cell.all)
Cell.randomize_mines()  
# for c in Cell.all:
#     print(c.is_mine)
# #Run the window
root.mainloop()
