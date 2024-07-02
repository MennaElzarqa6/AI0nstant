from tkinter import Button, Label
import random
import settings
import ctypes
import sys

class Cell:

    all = []                         # class attr. \ to append cell object
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None 
    def __init__(self,x,y,is_mine= False):
        self.is_mine = is_mine
        self.is_opened = False              ## check if cell is opened or not 
        self.is_mine_candidate = False 
        self.cell_btn_object = None
        self.x = x                           ## variables to give nums for cell as a name indicator  
        self.y = y
        
        #Append the object to the cell.all list
        Cell.all.append(self)              # accessing class attr inside of the class 
                                           # appending x,y,is_mine, .. == the class attr
                                           
    def create_btn_object(self,location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        btn.bind('<Button-1>',self.left_click_actions)                                    # .bind(the button, button function) 
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn
    
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text= f"cells left = {Cell.cell_count}",
            font=("",30)
        )
        Cell.cell_count_label_object = lbl


    def left_click_actions(self,event):                         ## Note ==>>>> event has to be entered as a second attr \ as it gives as info about the clicked button (location, state ,....)
        if self.is_mine:
            self.show_mine()
        else :
            if self.surrounded_cells_mines_length ==0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # if the cell mines counts equal the cells left count, player won
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0,'Congrats you won the game','Game over',0)
        #cancel left and right click events if the cell is already opened 
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')
    
    def show_mine(self):
        # A logic to interrupt the game and display a msg that player lost !
        self.cell_btn_object.config(bg='red')
        ctypes.windll.user32.MessageBoxW(0,'you clicked on a mine', 'Game over', 0)
        sys.exit()

    def get_cell_by_axis(self,x,y):
        # Return a cell object based on the value of x,y
        for cell in Cell.all:
            if (cell.x == x) and (cell.y == y):
                return cell 
    @property                       # read only attribute (same as ,x,y,is_mine)        
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x , self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y ),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x , self.y + 1),
        ]
        cells = [cell for cell in cells if cell is not None ]
        return cells
        


    @property
    def surrounded_cells_mines_length(self):
        counter =0 
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter 


    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1 
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # Replace the txt of cell count label with the newer count 
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text = f"Cells left :{Cell.cell_count}"
                    )
        # mark the cell as opened (use is as the last line of this method)
        self.is_opened = True 


    def right_click_actions(self,event):
        if not self.is_mine_candidate :
            self.cell_btn_object.configure(
                bg = "orange"
            )
            self.is_mine_candidate = True 
        else :
            self.cell_btn_object.configure(
                bg = "SystemButtonFace"
            )
            self.is_mine_candidate = False 

# ------------------------------- 
#                              >>>>>   static method <<<<<<<<<
    # creating an instant method 
    # thet belongs globally to the class,
    # not >> for each instance alone 
#----------------------------------
    @staticmethod 
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True 

#                              >>>>>   magic method <<<<<<<<<

    def __repr__(self):
        return f"cell({self.x},{self.y})"    # change the class object representation whenever called or printed  
