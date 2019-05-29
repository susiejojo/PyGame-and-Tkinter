import tkinter as tk
import math
from tkinter import messagebox
from math import *
r = tk.Tk() 
r.title('Welcome page') 
w = tk.Label(r, text='Game of squares', width=100, height=100, bg='yellow',font=('Verdana',40)) 
w.pack() 
r.after(2000, lambda: r.destroy()) 
r.mainloop()
r1=tk.Tk()
r1.title('Game Page')
tk.Label(r1, text="Enter no of squares:",width=50).pack()
entry = tk.Entry(r1)
entry.pack()
a=0
s = tk.Canvas(r1,width=1100, height=1100)
def clicked():
    s.delete("all")
    if (int(entry.get())>100):
        tk.messagebox.showinfo('Warning!','Limit Exceeded!')
    else:
        d1=0
        d2=0
        a=int(entry.get())
        sq=math.sqrt(a)
        sq=math.ceil(sq)
        no=900/sq
        #no=math.ceil(no)
        d3=no
        d4=no
        chk=0
        for i in range(1,a+1):
            s.create_rectangle(d1, d2, d3, d4, outline="blue",fill="green",width=1)
            s.pack()
            s.create_text(((d1+d3)/2,(d2+d4)/2),text=(str(i)))
            if ((d4+no>900)): # or d4!=900)):
                d1=d1+no
                d3=d3+no
                d2=0
                d4=no
                chk=2   
            else:
                d2+=no
                d4+=no
                chk=3
                
btn=tk.Button(r1,text="Go!",command=clicked)
btn.pack()
s.pack() 
r1.mainloop()
