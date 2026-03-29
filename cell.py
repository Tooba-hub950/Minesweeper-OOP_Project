from tkinter import Button, Label
import random
import settings             # randomly pick some elements
import ctypes
import sys
class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    def __init__(self,x,y, is_mine= False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_opened_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        
       # append the object to the cell.all list  
        Cell.all.append(self)
       
    def create_btn_object(self, location):
         btn = Button(
             location,
             width = 12,
             height = 4,
             text = f''
              
        ) 
        
         btn.bind('<Button-1>', self.left_click_actions)   # -1 for left click and -3 for right click
         btn.bind('<Button-3>', self.right_click_actions)
         self.cell_btn_object = btn  
        
    @staticmethod    
    def create_cell_count_label(location):
            lbl = Label(
                location,
                bg= 'light pink',
                fg= 'black', 
                text = f"Cells left:{Cell.cell_count}",
                font = ("", 25)
            )
            lbl.pack()
            Cell.cell_count_label_object = lbl  
        
    def left_click_actions(self, event):
        if self.is_opened:
            return
        
        if self.is_mine:
              self.show_mine()
        else:
              if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    if not cell_obj.is_opened and not cell_obj.is_mine:
                        cell_obj.left_click_actions(None)
                        
                self.show_cell()  
        # if mines count is equal to the cells left count, player won
        
              if Cell.cell_count ==  settings.MINES_COUNT:
                  ctypes.windll.user32.MessageBoxW(
                      0, 'Congragulations!! you won the game!', 'Game Over', 0
                      )
   
        # cancel left and right click events that is already opened    
        self.cell_btn_object.unbind('<Button-1>')      
        self.cell_btn_object.unbind('<Button-3>')   
             
    def get_cell_by_axis(self, x, y):                      
        # return a cell based on values of x nd y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell        # the reason is whenever i'm going to match in those x and y attributes, then i can immediately stop iteration and return to object
    
    @property
    def surrounded_cells(self):
              cells = [
                    self.get_cell_by_axis(self.x - 1, self.y - 1),
                    self.get_cell_by_axis(self.x - 1,   self.y),
                    self.get_cell_by_axis(self.x - 1, self.y + 1),
                    self.get_cell_by_axis(self.x,   self.y - 1),
                    self.get_cell_by_axis(self.x, self.y + 1),
                    self.get_cell_by_axis(self.x + 1, self.y - 1),
                    self.get_cell_by_axis(self.x + 1, self.y),
                    self.get_cell_by_axis(self.x + 1, self.y + 1)     
                ] 
              cells =  [cell for cell in cells if cell is not None] 
              return cells
             
    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self. surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter     
        
    
    def show_cell(self):
             if not self.is_opened:
            # 1. Update the logical count
                Cell.cell_count -= 1
            # 2. Update THIS specific button's appearance
            # We show the number of mines nearby
                self.cell_btn_object.configure(                
                    text=self.surrounded_cells_mines_length,
                    bg = 'light blue')
              
                if Cell.cell_count_label_object:
                    Cell.cell_count_label_object.configure(
                        text=f"Cells left: {Cell.cell_count}"
                )   
                self.is_opened = True
        
    def show_mine(self):  
    # a logic to interupt the game and display a message that player lost!
        self.cell_btn_object.configure(bg='powder blue')
        ctypes.windll.user32.MessageBoxW(0, 'you clicked on a mine', 'Game Over', 0)  # 0 is responsible to give only one option of a button to click , this line appers a message box if we replace 0 with 2 then 2 options appear like about and ignore
        sys.exit()            # it is a library
     
              
    def right_click_actions(self, event):
        if self.is_mine_candidate:
            return
        if not self.is_mine_candidate: 
            self.cell_btn_object.configure(bg = 'lavender')
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure( bg = 'SystemButtonFace')
            self.is_mine_candidate = False
        
    @staticmethod        # used as a decorator
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
            
    def __reper__(self):             # magic mehtod is responsible to change the way that object is being represented
        return  f"Cell({self.x}, {self.y})" 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
          