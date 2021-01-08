import tkinter as tk
import random
import time

def swap_two_pos(pos_0, pos_1):
    """This does the graphical swapping of the rectangles on the canvas
    by moving one rectangle to the location of the other, and vice versa
    """    
    
    x1, _, _, _ = canvas.coords(pos_0)
    x2, _, _, _ = canvas.coords(pos_1)
    
    diff = x1 - x2

    canvas.move(pos_0, -diff, 0)
    canvas.move(pos_1, +diff, 0)

def sort_two(pos_0, pos_1):
    x1, y1, _, _ = canvas.coords(pos_0)
    x2, y2, _, _ = canvas.coords(pos_1)

    diff = x1 - x2

    # moves each rectangle to the x position of the other; y remains unchanged
    if y2 < y1:
        canvas.move(pos_0, -diff, 0)
        canvas.move(pos_1, +diff, 0)
        return True
    else:
        return False

def rand_sort():
    for i in range(50000):
        rd1 = random.randint(0, 68)
        rd2 = random.randint(0, 68)
        pos_1 = barList[rd1]
        pos_2 = barList[rd2]
        if sort_two(pos_1, pos_2):
            barList[rd1], barList[rd2] = barList[rd2], barList[rd1]

def sort ():
    n = len(barList)
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1):
            if sort_two(barList[j], barList[j+1]):
                barList[j], barList[j+1] = barList[j+1], barList[j]
            
        window.update()
        time.sleep(0.1)
        
        
def random_swap():
    """Not a sort yet, but you have the bare bones operations
    so the swap is executed
    """
    for i in range(500):
        rd1 = random.randint(0, 68)
        rd2 = random.randint(0, 68)
        pos_0 = barList[rd1]
        pos_1 = barList[rd2]
        
        swap_two_pos(pos_0, pos_1)
        # it is necessary to swap the values in the list too
        barList[rd1], barList[rd2] = barList[rd2], barList[rd1]

def generate_colors():
    rgb_values = []
    rgb = (255, 0, 0)
    for i in range(23):
        rgb_values.append(rgb)
        rgb = 255, round(rgb[1] + 11), 0
    for i in range(23):
        rgb_values.append(rgb)
        rgb = round(rgb[0] - 11), 255, 0
    for i in range(24):
        rgb_values.append(rgb)
        rgb = 0, round(rgb[1] - 11), rgb[0] + 10
    return rgb_values

def from_rgb(tup):
    return "#%02x%02x%02x" % (tup[0], tup[1], tup[2])

colors = generate_colors()

window = tk.Tk()
window.title('Sorting')
window.geometry('1045x700')

# button to command the swap
tk.Button(window, text='swap', command=random_swap).pack()
tk.Button(window, text='sort', command=sort).pack()

xstart = 5
xend = 20
canvas = tk.Canvas(window, width='1045', height='700')
canvas.pack()
barList = []
lengthList = []
Y = 5

for x in range(1,70):
    bar = canvas.create_rectangle(xstart, Y, xend, 700, fill=from_rgb(colors[x]))
    barList.append(bar)
    xstart += 15
    xend += 15
    Y += 9

for bar in barList:
    x = canvas.coords(bar)
    length = x[3]-x[1]
    lengthList.append(length)

window.mainloop()