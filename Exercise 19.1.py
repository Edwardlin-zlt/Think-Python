from swampy.Gui import *

g = Gui()
g.title("Exercise 19.1")
canvas = g.ca(width=500, height=500)
canvas.config(bg='black')
item = canvas.circle([0, 0], 100, fill='red')
def callback1():
    g.bu(text='Now Press me', command=callback2)

def callback2():
    g.la(text='Thanks')

g.bu(text='Press me', command=callback1)

g.mainloop()