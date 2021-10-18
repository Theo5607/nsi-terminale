from tkinter import *

#importation de la classe Polynomial et de la fonction mult_scal
from polynome import Polynomial
from polynome import mult_scal

#création de la fenêtre
fenetre = Tk()
fenetre.geometry("600x400")

#création de la frame1 qui gère les boutons
Frame1 = Frame(fenetre, relief=GROOVE)
Frame1.pack(side=BOTTOM, pady=30)

#variables utilisées dans les boutons
liste_nb=['0','1','2','3','4','5','6','7','8','9','-1','-2','-3','-4','-5','-6','-7','-8','-9']
new_poly=[]
new_poly_other=[]
str_afficher=['','','',0]

def which_button(button_press):
   """
   fonction qui gère l'affichage de l'écran par rapport aux boutons cliqués. Prend en paramètres une string renseignée dans le bouton cliqué
   """

   #boutons de nombre
   for el in liste_nb:
      if el==button_press and str_afficher[3]==0 and (len(new_poly)<10 and len(new_poly_other)<10):
         if str_afficher[1]=='':
            new_poly.append(int(button_press))
            poly = Polynomial(new_poly)
            Label1.configure(text=poly.to_string())
         else:
            poly = Polynomial(new_poly)
            
            new_poly_other.append(int(button_press))
            poly_other = Polynomial(new_poly_other)
            Label1.configure(text=poly.to_string()+str_afficher[1]+poly_other.to_string())
            
   if str_afficher[3]==1:
      for i in range(0,10):
         if liste_nb[i]==button_press:
            poly = Polynomial(new_poly)
            Label1.configure(text='('+poly.to_string()+')^'+button_press)
            str_afficher[3]=10+int(button_press)
   elif str_afficher[3]==2:
      for el in liste_nb:
         if el==button_press:
            poly = Polynomial(new_poly)
            Label1.configure(text=button_press+'('+poly.to_string()+')')
            str_afficher[3]=30+int(button_press)

   #bouton C: supprime le dernier élément entré
   if button_press=='C':
      el_supp=''
      if str_afficher[3]!=0:
         poly = Polynomial(new_poly)
         Label1.configure(text=poly.to_string())
         str_afficher[3]=0
         
      elif len(new_poly_other)>0:
         el_supp=new_poly_other.pop(-1)
         if len(new_poly_other)==0:
            str_afficher[1]=''
            poly = Polynomial(new_poly)
            Label1.configure(text=poly.to_string())
         else:
            poly = Polynomial(new_poly)
            poly_other = Polynomial(new_poly_other)
            Label1.configure(text=poly.to_string()+str_afficher[1]+poly_other.to_string())
            
      elif str_afficher[1]!='':
         str_afficher[1]=''
         poly = Polynomial(new_poly)
         Label1.configure(text=poly.to_string())
         
      elif len(new_poly)>0:
         el_supp=new_poly.pop(-1)
         poly = Polynomial(new_poly)
         Label1.configure(text=poly.to_string())
         if len(new_poly)==0:
            Label1.configure(text="Entrez une valeur")
      else:
         Label1.configure(text="Entrez une valeur")

   #bouton AC: supprime toute la fonction
   elif button_press=='AC':
      for i in range(3):
         str_afficher[i]=''
      new_poly.clear()
      new_poly_other.clear()
      str_afficher[3]=0
      Label1.configure(text="Entrez une valeur")

   #bouton +
   elif button_press=='+':
      if str_afficher[1]=='' and len(new_poly)!=0 and str_afficher[3]==0:
         str_afficher[1]=' + '

         poly = Polynomial(new_poly)
         poly_other = Polynomial(new_poly_other)
               
         Label1.configure(text=poly.to_string()+str_afficher[1])

   #bouton -
   elif button_press=='-':
      if str_afficher[1]=='' and len(new_poly)!=0 and str_afficher[3]==0:
         str_afficher[1]=' - '

         poly = Polynomial(new_poly)
         poly_other = Polynomial(new_poly_other)
               
         Label1.configure(text=poly.to_string()+str_afficher[1])

   #bouton *
   elif button_press=='*':
      if str_afficher[1]=='' and len(new_poly)!=0 and str_afficher[3]==0:
         str_afficher[1]=' * '

         poly = Polynomial(new_poly)
         poly_other = Polynomial(new_poly_other)
               
         Label1.configure(text=poly.to_string()+str_afficher[1])

   #bouton pour les puissances
   elif button_press=='Pow':
      if str_afficher[1]=='' and len(new_poly)!=0:
         poly = Polynomial(new_poly)
         Label1.configure(text='('+poly.to_string()+')^[]')

         str_afficher[3]=1

   #bouton pour la multiplication par un scalaire
   elif button_press=='Sca':
      if str_afficher[1]=='' and len(new_poly)!=0:
         poly = Polynomial(new_poly)
         Label1.configure(text='[]('+poly.to_string()+')')

         str_afficher[3]=2

   #bouton pour dériver
   elif button_press=='Der':
      if str_afficher[1]=='' and len(new_poly)!=0:
         poly = Polynomial(new_poly)
         Label1.configure(text='('+poly.to_string()+")'")

         str_afficher[3]=3

   #bouton pour afficher le résultat
   elif button_press=='=':
      if str_afficher[1]!='':
         poly = Polynomial(new_poly)
         poly_other = Polynomial(new_poly_other)
         if str_afficher[1]==' + ':
            poly_add=poly+poly_other
         elif str_afficher[1]==' - ':
            poly_add=poly-poly_other
         elif str_afficher[1]==' * ':
            poly_add=poly*poly_other
         new_poly.clear()
         for el in poly_add.lpolynome:
            new_poly.append(el)
         poly_add.lpolynome
         new_poly_other.clear()
         str_afficher[1]=''

         Label1.configure(text=poly_add.to_string())
         
      elif str_afficher[3]>=10 and str_afficher[3]<=19:
         poly = Polynomial(new_poly)
         poly_pow = (Polynomial(new_poly)**(str_afficher[3]-10)).lpolynome
         new_poly.clear()
         for el in poly_pow:
            new_poly.append(el)

         poly = Polynomial(new_poly)
         Label1.configure(text=poly.to_string())
         str_afficher[3]=0

      elif str_afficher[3]>=21 and str_afficher[3]<=39:
         list_scal = mult_scal(new_poly,str_afficher[3]-30)
         poly = Polynomial(list_scal)
         new_poly.clear()
         for el in list_scal:
            new_poly.append(el)

         poly = Polynomial(new_poly)
         Label1.configure(text=poly.to_string())
         str_afficher[3]=0

      elif str_afficher[3]==3:
         poly = Polynomial(new_poly)
         poly.derivative()
         new_poly.clear()
         for el in poly.lpolynome:
            new_poly.append(el)
            
         Label1.configure(text=poly.to_string())
         str_afficher[3]=0

      if new_poly==[]:
         Label1.configure(text='0')

#affichage des boutons 1 à 9
nb=1
for ligne in range(3):
    for colonne in range(3):            
        Button(Frame1, text=str(nb), command=lambda m=str(nb): which_button(m), borderwidth=1, height=2, width=5).grid(row=ligne, column=colonne)
            
        nb+=1

#affichage des boutons -1 à -9
nb=-1
for ligne in range(3):
    for colonne in range(3,6):            
        Button(Frame1, text=str(nb), command=lambda m=str(nb): which_button(m), borderwidth=1, height=2, width=5).grid(row=ligne, column=colonne)
            
        nb-=1

#affichage des autres boutons
Button(Frame1, text='C', command=lambda m='C': which_button(m), borderwidth=1, height=2, width=5).grid(row=4, column=5)
Button(Frame1, text='0', command=lambda m='0': which_button(m), borderwidth=1, height=2, width=5).grid(row=4, column=0)
Button(Frame1, text='AC', command=lambda m='AC': which_button(m), borderwidth=1, height=2, width=5).grid(row=4, column=4)

Button(Frame1, text='+', command=lambda m='+': which_button(m), borderwidth=1, height=2, width=5).grid(row=0, column=6)
Button(Frame1, text='-', command=lambda m='-': which_button(m), borderwidth=1, height=2, width=5).grid(row=1, column=6)
Button(Frame1, text='*', command=lambda m='*': which_button(m), borderwidth=1, height=2, width=5).grid(row=2, column=6)

Button(Frame1, text='Pow', command=lambda m='Pow': which_button(m), borderwidth=1, height=2, width=5).grid(row=4, column=1)
Button(Frame1, text='Der', command=lambda m='Der': which_button(m), borderwidth=1, height=2, width=5).grid(row=4, column=2)
Button(Frame1, text='Sca', command=lambda m='Sca': which_button(m), borderwidth=1, height=2, width=5).grid(row=4, column=3)

Button(Frame1, text='=', command=lambda m='=': which_button(m), borderwidth=1, height=2, width=5).grid(row=4, column=6)

#affichage de la frame2 dans laquelle est affichée l'expression
Frame2 = Frame(fenetre, height=3, width=100, borderwidth=2, relief=GROOVE, background='white')
Frame2.pack(side=LEFT, padx=20, ipady=10)
Label1 = Label(Frame2, text="Entrez une valeur", height=2, width=100, bg='white', font=("Times New Roman", 12))
Label1_pack=Label1.pack(padx=20, ipady=10)

#boucle infinie de la fenetre tkinter
fenetre.mainloop()
