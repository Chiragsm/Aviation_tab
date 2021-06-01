from tkinter import *
from serone import *
import time

time_string = time.strftime('%H:%M')



window = Tk()
pic = PhotoImage(file="A_logo_1.PNG")
window.iconphoto(False, pic)

se = But_comm()
window.title("Aviation Tab System")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20, bg="#F0F8FF")


my_label = Label(text="Aviation Tab System", bg="#F0F8FF", fg="#000000", font=("Ink Free", 20, "bold"))
my_label.pack()

ascend_b = Button(text="Ascend", width=15, bg="#F0FFFF", fg="#000000", font=("Ink Free", 12, "bold"), command=se.a_but)
ascend_b.place(x=20, y=80)

cruise_b = Button(text="Cruise", width=15, bg="#F0FFFF", fg="#000000", font=("Ink Free", 12, "bold"), command=se.c_but)
cruise_b.place(x=20, y=120)

descend_b = Button(text="Descend", width=15, bg="#F0FFFF", fg="#000000", font=("Ink Free", 12, "bold"), command=se.d_but)
descend_b.place(x=20, y=160)

reset_b = Button(text="Reset", width=15, bg="#F0FFFF", fg="#000000", font=("Ink Free", 12, "bold"), command=se.re_but)
reset_b.place(x=150, y=210)

my_var = Label(text=time_string, width= 10, height=2, bg="#F0F8FF", fg="#00E600", font=("Ariel", 15, "bold"))
my_var.place(x=360, y=200)

canvas = Canvas(width=120, height=100, bg="#000000")
Logo = PhotoImage(file="aero_logo.png")
canvas.create_image(65, 50, image=Logo)
canvas.place(x=280, y=80)

window.mainloop()