from tkinter import *
import random
class Window:
    def __init__(self, master):

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
                           x2-radius, y2,
                           x1+radius, y2,
                           x1+radius, y2,
                           x1, y2,
                           x1, y2-radius,
                           x1, y2-radius,
                           x1, y1+radius,
                           x1, y1+radius,
                           x1, y1]
            return self.c.create_polygon(points, **kwargs, smooth=True)

        def generate_colors(n):
            rgb_values = [] 
            hex_values = [] 
            r = int(random.random() * 256) 
            g = int(random.random() * 256) 
            b = int(random.random() * 256) 
            step = 256 / n 
            for _ in range(n): 
                r += step 
                g += step 
                b += step 
                r = int(r) % 256 
                g = int(g) % 256 
                b = int(b) % 256 
                r_hex = hex(r)[2:] 
                g_hex = hex(g)[2:] 
                b_hex = hex(b)[2:] 
                hex_values.append('#' + r_hex + g_hex + b_hex) 
                rgb_values.append((r,g,b)) 
            return rgb_values

        self.c = Canvas(width=940, height=650, bg='white')


        colors = generate_colors(42)
        print(colors)
        x_counter = 10
        sticks = {}
        for i in range(41):
            sticks[i] = [round_rect(x_counter, 400, x_counter+20, 600, radius=10, fill=from_rgb(colors[i]))]
            x_counter += 22.5

        def info(event):
            self.toplevel = Toplevel(bg='white')
            self.toplevel.transient()
            self.frame = Frame(self.toplevel, width=400, height=300)
            self.toplevel.title("Program info")
            Label(self.toplevel, text='bubble sort', bg='white', fg='black').pack(pady=20)
            Label(self.toplevel, text="abimbola idunnuoluwa programed this",
                bg='white', fg='black').pack()
            Label(self.toplevel, text="bubble sort algorithm implemented in python tkinter",
                bg='white', fg='black').pack()
            Label(self.toplevel, text="thank you :-)",
                bg='white', fg='black').pack()
            Button(self.toplevel, text="close",
                command=self.toplevel.withdraw).pack(pady=30)

        def sort(event):
            """
            docstring
            """
            self.toplevel = Toplevel(bg='white')
            self.toplevel.transient()
            self.frame = Frame(self.toplevel, width=400, height=300)
            self.toplevel.title("sorting")
            Label(self.toplevel, text='bubble sort', bg='white', fg='black').pack(pady=20)
            Label(self.toplevel, text="sorting",
                bg='white', fg='black').pack()
            Button(self.toplevel, text="close",
                command=self.toplevel.withdraw).pack(pady=30)

        def rd(event):
            """
            docstring
            """
            self.toplevel = Toplevel(bg='white')
            self.toplevel.transient()
            self.frame = Frame(self.toplevel, width=400, height=300)
            self.toplevel.title("sorting")
            Label(self.toplevel, text='bubble sort', bg='white', fg='black').pack(pady=20)
            Label(self.toplevel, text="randomizing",
                bg='white', fg='black').pack()
            Button(self.toplevel, text="close",
                command=self.toplevel.withdraw).pack(pady=30)

        def infoenter(event):
            self.c.itemconfig(infoBtn, fill='grey50')

        def infoleave(event):
            self.c.itemconfig(infoBtn, fill='grey70')
            
        infoBtn = round_rect(10, 10, 310, 110, fill='grey70')
        infoTxt = self.c.create_text(80, 80, text='Info', font='helvetica 48', fill='white')
        self.c.tag_bind(infoBtn, '<ButtonPress-1>', info)
        self.c.tag_bind(infoTxt, '<ButtonPress-1>', info)
        self.c.tag_bind(infoBtn, '<Enter>', infoenter)
        self.c.tag_bind(infoTxt, '<Enter>', infoenter)
        self.c.tag_bind(infoBtn, '<Leave>', infoleave)
        self.c.tag_bind(infoTxt, '<Leave>', infoleave)

        def sortenter(event):
            self.c.itemconfig(sortBtn, fill='grey50')

        def sortleave(event):
            self.c.itemconfig(sortBtn, fill='grey70')

        sortBtn = round_rect(320, 10, 620, 110, fill='grey70')
        sortTxt = self.c.create_text(380, 80, text='sort', font='helvetica 48', fill='white')
        self.c.tag_bind(sortBtn, '<ButtonPress-1>', sort)
        self.c.tag_bind(sortTxt, '<ButtonPress-1>', sort)
        self.c.tag_bind(sortBtn, '<Enter>', sortenter)
        self.c.tag_bind(sortTxt, '<Enter>', sortenter)
        self.c.tag_bind(sortBtn, '<Leave>', sortleave)
        self.c.tag_bind(sortTxt, '<Leave>', sortleave)

        def rdenter(event):
            self.c.itemconfig(rdBtn, fill='grey50')

        def rdleave(event):
            self.c.itemconfig(rdBtn, fill='grey70')

        rdBtn = round_rect(630, 10, 930, 110, fill='grey70')
        rdTxt = self.c.create_text(780, 80, text='randomize', font='helvetica 48', fill='white')
        self.c.tag_bind(rdBtn, '<ButtonPress-1>', rd)
        self.c.tag_bind(rdTxt, '<ButtonPress-1>', rd)
        self.c.tag_bind(rdBtn, '<Enter>', rdenter)
        self.c.tag_bind(rdTxt, '<Enter>', rdenter)
        self.c.tag_bind(rdBtn, '<Leave>', rdleave)
        self.c.tag_bind(rdTxt, '<Leave>', rdleave)

        self.c.pack()

    

    


root = Tk()

ex4 = Window(root)

root.title('Bubble sort')

print('sorting')
root.mainloop()  




        
