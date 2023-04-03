import random
import tkinter as tk

GUI = tk.Tk()

GUI.geometry('600x600')

GUI.config(bg='#EEFC5E')

GUI.resizable(width=False,height=False)

GUI.title('สุ่มเลข สลากกินแบ่งรัฐบาล')

def generate_number():

    list = ['0','1','2','3','4','5','6','7','8','9']

    number = ''

    for i in range(6):

        number = number + random.choice(list)

    L2.config(text = number) 

    number1 = ''
    for j in range(3):

        number1 = number1 + random.choice(list)

    L40.config(text = number1) 

    number2 = ''
    for k in range(3):

        number2 = number2 + random.choice(list)

    L50.config(text = number2) 

    number3 = ''
    for l in range(2):

        number3 = number3 + random.choice(list)

    L60.config(text = number3) 
 

L1 = tk.Label(text='สุ่มเลขซื้อสลากกินแบ่งรัฐบาล',font=('Arial',30),bg='black',fg='white')
L1.place(x=80,y=20)
 

B1 = tk.Button(text='คลิกสุ่มเลข',font=('Arial',25),command=generate_number)
B1.place(x=200,y=450)

 

L2 = tk.Label(bg='#EEFC5E',font=('Arial',30),text='')
L2.place(x=280,y=130)

L40 = tk.Label(bg='#EEFC5E',font=('Arial',30),text='')
L40.place(x=280,y=200)

L50 = tk.Label(bg='#EEFC5E',font=('Arial',30),text='')
L50.place(x=280,y=270)

L60 = tk.Label(bg='#EEFC5E',font=('Arial',30),text='')
L60.place(x=280,y=340)

################################################################################
 
L3 = tk.Label(text='รางวัลที่ 1',font=('Arial',30),bg='#FF0014',fg='white')
L3.place(x=70,y=130)
 
L4 = tk.Label(text='เลขหน้า 3 ตัว',font=('Arial',30),bg='#0019FF',fg='white')
L4.place(x=10,y=200)

L5 = tk.Label(text='เลขท้าย 3 ตัว',font=('Arial',30),bg='#12FFA7',fg='white')
L5.place(x=10,y=270)

L6 = tk.Label(text='เลขท้าย 2 ตัว',font=('Arial',30),bg='#FF7300',fg='white')
L6.place(x=10,y=340)
 

GUI.mainloop()