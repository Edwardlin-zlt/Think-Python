from swampy.Gui import *

g = Gui()
g.title('Exercise 19.2')

def d_circle():
    canvas.circle([0, 0], 100, fill='yellow')


canvas = g.ca(width=500, height=500, bg='black')
canvas.oval([[0, 0], [200, 100]], outline='orange', width=1)
entry = g.en(text='Default text')
text = g.te(width=100, height=5)
g.mainloop()