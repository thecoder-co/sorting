import tkinter as tk
import random


def swap_two_pos(pos_0, pos_1):
    """This does the graphical swapping of the rectangles on the canvas
    by moving one rectangle to the location of the other, and vice versa
    """    
    x_00, _, x_01, _ = canvas.coords(pos_0)
    x_10, _, x_11, _ = canvas.coords(pos_1)
    # moves each rectangle to the x position of the other; y remains unchanged
    canvas.move(pos_0, x_10-x_00, 0)
    canvas.move(pos_1, x_01-x_11, 0)

def sort_two(pos_0, pos_1):
    x_00, y1, x_01, _ = canvas.coords(pos_0)
    x_10, y2, x_11, _ = canvas.coords(pos_1)
    # moves each rectangle to the x position of the other; y remains unchanged
    if y2 > y1:
        canvas.move(pos_0, x_10-x_00, 0)
        canvas.move(pos_1, x_01-x_11, 0)

def rand_sort():
    for i in range(50000):
        rd1 = random.randint(0, 58)
        rd2 = random.randint(0, 58)
        pos_1 = barList[rd1]
        pos_2 = barList[rd2]
        sort_two(pos_1, pos_2)
        barList[rd1], barList[rd2] = barList[rd2], barList[rd1]



def sort ():
    n = len(barList)
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1):
                sort_two(barList[j], barList[j+1])
                barList[j], barList[j+1] = barList[j+1], barList[j]
        else:
            break

def random_swap():
    """Not a sort yet, but you have the bare bones operations
    so the swap is executed
    """
    for i in range(500):
        rd1 = random.randint(0, 58)
        rd2 = random.randint(0, 58)
        pos_0 = barList[rd1]
        pos_1 = barList[rd2]
        
        swap_two_pos(pos_0, pos_1)
        # it is necessary to swap the values in the list too
        barList[rd1], barList[rd2] = barList[rd2], barList[rd1]

window = tk.Tk()
window.title('Sorting')
window.geometry('600x400')

# button to command the swap
tk.Button(window, text='swap', command=random_swap).pack()
tk.Button(window, text='sort', command=sort).pack()

xstart = 5
xend = 15
canvas = tk.Canvas(window, width='900', height='900')
canvas.pack()
barList = []
lengthList = []
Y = 5

for x in range(1,60):
    bar = canvas.create_rectangle(xstart, Y, xend, 395, fill='red')
    barList.append(bar)
    xstart += 10
    xend += 10
    Y += 5

for bar in barList:
    x = canvas.coords(bar)
    length = x[3]-x[1]
    lengthList.append(length)

window.mainloop()