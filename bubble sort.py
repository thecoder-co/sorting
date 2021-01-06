from tkinter import *
import random
def from_rgb(tup):
    return "#%02x%02x%02x" % (tup[0], tup[1], tup[2])

def quit(event):
    sys.exit()

def round_rect(x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]
    return c.create_polygon(points, **kwargs, smooth=True)

def generate_colors():
    rgb_values = []
    rgb = (255, 0, 0)
    for i in range(30):
        rgb_values.append(rgb)
        rgb = 255, round(rgb[1] + 8), 0
    for i in range(32):
        rgb_values.append(rgb)
        rgb = round(rgb[0] - 8), 255, 0
    return rgb_values

def random_sort():
    """Not a sort yet, but you have the bare bones operations
    so the swap is executed
    """
    pos_0 = random.sample(barList, 1)
    pos_1 = random.sample(barList, 1)
    swap_two_pos(pos_0, pos_1)
    # it is necessary to swap the values in the list too
    barList[10], barList[20] = barList[20], barList[10]


def swap_two_pos(pos_0, pos_1):
    """This does the graphical swapping of the rectangles on the canvas
    by moving one rectangle to the location of the other, and vice versa
    """
    """print(pos_0[0])
    print(pos_1[0])
    x_00, _, x_01, _ = c.coords(pos_0[0])
    x_10, _, x_11, _ = c.coords(pos_1[0])
    # moves each rectangle to the x position of the other; y remains unchanged
    c.move(pos_0, x_10-x_00, 0)
    c.move(pos_1, x_01-x_11, 0)"""

    print(c.coords(bar))


c = Canvas(width=940, height=650, bg='white')



colors = generate_colors()

xstart = 15
xend = 30
barList = []
lengthList = []

# creates a dictionary of shapes in sticks
"""
for i in range(41):
sticks.append([round_rect(x_counter, 400, x_counter+20, 600, radius=10,
fill=from_rgb(colors[i])), x_counter, 400, x_counter+20, 600, i])
x_counter += 22.5
"""

bar = c.create_rectangle(10, 100, 10, 100)

y = 200
for x in range(1, 62):
    bar = round_rect(
            xstart, y, xend, 600, fill=from_rgb(colors[x]),radius=20)
    barList.append(bar)
    xstart += 15
    xend += 15
    y += 6

def info(event):
    toplevel = Toplevel(bg='white')
    toplevel.transient()
    frame = Frame(toplevel, width=400, height=300)
    toplevel.title("Program info")
    Label(toplevel, text='bubble sort',
            bg='white', fg='black').pack(pady=20)
    Label(toplevel, text="abimbola idunnuoluwa programed this",
            bg='white', fg='black').pack()
    Label(toplevel, text="bubble sort algorithm implemented in python tkinter",
            bg='white', fg='black').pack()
    Label(toplevel, text="thank you :-)",
            bg='white', fg='black').pack()
    Button(toplevel, text="close",
            command=toplevel.withdraw).pack(pady=30)

def sort(event):
    """
    docstring
    """
    toplevel = Toplevel(bg='white')
    toplevel.transient()
    frame = Frame(toplevel, width=400, height=300)
    toplevel.title("sorting")
    Label(toplevel, text='bubble sort',
            bg='white', fg='black').pack(pady=20)
    Label(toplevel, text="sorting",
            bg='white', fg='black').pack()
    Button(toplevel, text="close",
            command=toplevel.withdraw).pack(pady=30)

# this is the code that is not working, it's probably because i wrote it wrong
# help me correct it
# the code is supposed to pick two random sticks and exchange their place

def rd(event):
    """
    docstring
    """
    rd1 = random.randint(0, 40)
    rd2 = random.randint(0, 40)
    """
    item1 = tuple(sticks[rd1][1:])
    item2 = tuple(sticks[rd2][1:])
    c.move(sticks[rd1][0], sticks[rd1][1]-sticks[rd2][1], 0)
    c.move(sticks[rd2][0], sticks[rd2][1]-sticks[rd1][1], 0)
    sticks[rd1][1:] = item2[0:]
    sticks[rd2][1:] = item1[0:]"""
    random_sort()

def infoenter(event):
    c.itemconfig(infoBtn, fill='grey50')

def infoleave(event):
    c.itemconfig(infoBtn, fill='grey70')

infoBtn = round_rect(10, 10, 310, 110, fill='grey70')
infoTxt = c.create_text(
        80, 80, text='Info', font='helvetica 48', fill='white')
c.tag_bind(infoBtn, '<ButtonPress-1>', info)
c.tag_bind(infoTxt, '<ButtonPress-1>', info)
c.tag_bind(infoBtn, '<Enter>', infoenter)
c.tag_bind(infoTxt, '<Enter>', infoenter)
c.tag_bind(infoBtn, '<Leave>', infoleave)
c.tag_bind(infoTxt, '<Leave>', infoleave)

def sortenter(event):
    c.itemconfig(sortBtn, fill='grey50')

def sortleave(event):
    c.itemconfig(sortBtn, fill='grey70')

sortBtn = round_rect(320, 10, 620, 110, fill='grey70')
sortTxt = c.create_text(
        380, 80, text='sort', font='helvetica 48', fill='white')
c.tag_bind(sortBtn, '<ButtonPress-1>', sort)
c.tag_bind(sortTxt, '<ButtonPress-1>', sort)
c.tag_bind(sortBtn, '<Enter>', sortenter)
c.tag_bind(sortTxt, '<Enter>', sortenter)
c.tag_bind(sortBtn, '<Leave>', sortleave)
c.tag_bind(sortTxt, '<Leave>', sortleave)

def rdenter(event):
    c.itemconfig(rdBtn, fill='grey50')

def rdleave(event):
    c.itemconfig(rdBtn, fill='grey70')

rdBtn = round_rect(630, 10, 930, 110, fill='grey70')
rdTxt = c.create_text(
        780, 80, text='randomize', font='helvetica 48', fill='white')
c.tag_bind(rdBtn, '<ButtonPress-1>', rd)
c.tag_bind(rdTxt, '<ButtonPress-1>', rd)
c.tag_bind(rdBtn, '<Enter>', rdenter)
c.tag_bind(rdTxt, '<Enter>', rdenter)
c.tag_bind(rdBtn, '<Leave>', rdleave)
c.tag_bind(rdTxt, '<Leave>', rdleave)

c.pack()

    

    


root = Tk()


root.title('Bubble sort')

print('sorting')
root.mainloop()  




        
