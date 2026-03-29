# there is a great time to separate our files for all constants, and have and atleast some variables stored in somewhere so we created another file because that might be too much information that needs to be stored in one file
import settings
width = 1440
height = 720
grid_size = 6  
# formula to calcultae how many mines we want to used in our games
CELL_COUNT= grid_size ** 2
MINES_COUNT = (CELL_COUNT) // 4        