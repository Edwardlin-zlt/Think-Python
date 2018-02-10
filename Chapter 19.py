from Gui import *

def make_label():
    g.la(text='Thank you')

g = Gui()
g.title('Pyfundtool')
label = g.la(text="Press the botton")
button = g.bu(text='Press me.')
button2 = g.bu(text='No, press me.', command=make_label)



g.mainloop()

