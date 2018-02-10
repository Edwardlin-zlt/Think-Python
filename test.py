from swampy.Gui import *

g = Gui()
g.title("")

def callback1():
    g.bu(text='Now press me', command=callback2)

def callback2():
    g.la(text='Thanks')

g.bu(text='Press me', command=callback1)

g.mainloop()