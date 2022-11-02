from tkinter import *
from tkinter import messagebox #import message box library

def click():
    # messagebox.showinfo(title='This is an info message box',
    #                     message='There is an error')
   # while(True):
   #  messagebox.showwarning(title='WARNING',
   #                         message='You have a virus!')
   #  messagebox.showerror(title='Error',message="Something went wrong!")
   #  if messagebox.askokcancel(title="Ask Ok Cancel",message="Do you want to do the thing?"):
   #      print("You did a thing!")
   #  else:
   #      print("You canceled a thing!")
   #  if messagebox.askretrycancel(title="ask ok cancel",message="Do you want to rety the thing?"):
   #      print("You retried a thing!")
   #  else:
   #      print("You canceled a thing again! :(")
   #  if messagebox.askyesno(title="ask yes or no",message="Do you like cake?"):
   #      print("I like cake too.")
   #  else:
   #      print("Why do you not like cake???")
   #  answer = messagebox.askquestion(title='ask question',message='Do you like pie?')
   #  if(answer == 'yes'):
   #      print('I like pie too :)')
   #  else:
   #      print('What is wrong with you, why dony you like pie??? :(')
   answer = (messagebox.askyesnocancel(title='Yes no cancel',message='Do you like to code?',icon='info'))
   if(answer==True):
       print("You like to code!")
   elif(answer==False):
       print("Why not? You should get into it!")
   else:
       print("Why are you dodging????")

window = Tk()

button = Button(window,command=click,text='Click Me',
                font=("Arial",25,"bold"))
button.pack()

window.mainloop()