from swampy.Gui import *

g = Gui()
g.title("Exercise 19.2")

def d_circle():
    global circle
    circle = canvas.circle([0, 0], 100, fill='yellow')

def change_color():
    global circle
    color = entry.get()
    circle.config(fill=color)


canvas = g.ca(width=500, height=500, bg='black')
button = g.bu(text="Press me", command=d_circle)
entry = g.en(text='default text')
button2 = g.bu(text='Change color', command=change_color)

g.mainloop()