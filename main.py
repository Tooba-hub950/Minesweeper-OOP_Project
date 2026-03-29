# TK inter is very great library to pratice  because it comes with a lot of useful classes that we are going to instantiate to create our window
from tkinter import *
from cell import Cell
from settings import settings
import utils
# import settings


root = Tk( )          # root is a variable
#override the settings of window
root.configure( bg= "powderblue")              # to configure the background color
root.geometry(f'{settings.width}x{settings.height}')    # to change  the size of window
root.title("Minesweeper Game")  # tiltle method change our title
root.resizable(False, False)    # one for width and one for height

# frame is a container to add more elements in future like buttons , lables
top_frame =   Frame(
    root,
    bg = "mistyrose",
    width= settings.width,
    height= utils.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg = 'lavender',
    fg = 'black',
    text = 'Minesweeper Game',
    font = ('', 30)
    )
game_title.place(
     x = utils.width_prct(20), y = 0

 )

left_frame = Frame(
    root,
    bg = "lavender",
    width =utils.width_prct(25),
    height =utils.height_prct(75)
)
left_frame.place( x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg = 'thistle',
    width =utils.width_prct(75),
    height =utils.height_prct(75)
    )

center_frame.place(
    x = utils.width_prct(25),
    y =utils.height_prct(25)
    )
btn1 = Button(
    center_frame,
    bg = 'honeydew',
    text ='First Button'
)
btn1.place( x=0, y=0) 

for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
            
       ) 
# call the label form cell class  
Cell.create_cell_count_label(left_frame)     
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()        
 # run the window                                      
root.mainloop()
