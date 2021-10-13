from tkinter import *

fenetre = Tk()
fenetre.geometry("600x400")

Frame1 = Frame(fenetre, relief=GROOVE)
Frame1.pack(side=BOTTOM, pady=30, ipadx=200)

def which_button(button_press):
   print (button_press)

nb=1
for ligne in range(3):
    for colonne in range(3):            
        Button(Frame1, text=str(nb), command=lambda m=str(nb): which_button(m), borderwidth=1, height=2, width=5).grid(row=ligne, column=colonne)
            
        nb+=1
        
Button(Frame1, text='C', borderwidth=1, height=2, width=5).grid(row=3, column=0)

Button(Frame1, text='0', borderwidth=1, height=2, width=5).grid(row=3, column=1)

Button(Frame1, text='AC', borderwidth=1, height=2, width=5).grid(row=3, column=2)

Frame2 = Frame(fenetre, height=3, width=100, borderwidth=2, relief=GROOVE, background='white')
Frame2.pack(side=LEFT, padx=20, ipady=10)
Label(Frame2, text="Frame 2", height=3, width=100).pack(padx=20, ipady=10)

fenetre.mainloop()