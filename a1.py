from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')


upload = Image.open("app_img.jpg")

upload= upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='lightblue')
label.place(x=180, y=20)

label1= Label(root,
text="hey user! Welcome to Denomination Counter Application ",
bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)


def msg():
   msgbox=messagebox.showinfo("alert","do you want to calculate the denomination count ") 
   if msgbox=="ok":
      topwin()

Button1=Button(root,text="lets get started",command=msg,bg="brown",fg="white")
Button1.place(x=260,y=360)

def topwin():
   top=Toplevel()
   top.title("denomination calculation")
   top.geometry("600x350")
   top.configure(bg="light grey")
   label=Label(top,text="entre the amount",bg="light grey")
   
   entry=Entry(top)
   lbl=Label(top,text="here are the number of notes or each denomination",bg="light grey")
   l1=Label(top,text="2000",bg="light grey")
   l2=Label(top,text="500",bg="light grey")
   l3=Label(top,text="100",bg="light grey")

   t1=Entry(top)
   t2=Entry(top)
   t3=Entry(top)  

   btn = Button(top, text='Calculate', command=calculator, bg='brown', fg='white')

# Centering Widgets in the Top Window

   label.place(x=230, y=50)

   entry.place(x=200, y=80)

   btn.place(x=240, y=120)

   lbl.place(x=140, y=170)

   l1.place(x=180, y=200)

   l2.place(x=180, y=230)

   l3.place(x=180, y=260)

   t1.place(x=270, y=200)

   t2.place(x=270, y=230)

   t3.place(x=270, y=260)

   top.mainloop()   

root.mainloop()
   