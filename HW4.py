from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
from tkinter import messagebox
####################### CSV #######################################
import csv

def writecsv(datalist):
    with open('my expense.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer 
        fw.writerow(datalist) 


def readcsv():
    with open('my expense.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader 
        data = list(fr)
    return data

###################################################################

GUI = Tk() # นี่่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
GUI.geometry('850x500') #นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='MY EXPENSE',font=('Angsana New',30),fg='Black')
L1.pack()

LF1 = ttk.LabelFrame(GUI,text='Fill in the information')
LF1.place(x=10,y=100)

v_data = StringVar() # ตัวแปรพิเศษที่ใช้กับข้อความใน GUI
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',16))
E1.pack(pady=10,padx=10,ipady=5,ipadx=100)


from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%y/%m/%d %H:%M:%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] #[เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง CSV
    v_data.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก
    
    
    text2 = 'Successful done'
    messagebox.showinfo('Record',text2)


B2 = ttk.Button(LF1,text='Record',command=SaveData)
B2.pack(pady=10,padx=10,ipadx=20,ipady=20)


######################################################################

LF2 = ttk.LabelFrame(GUI, text='EXPENSE')
LF2.place(x=400, y=100)

text = Text(LF2, font=('TH Sarabun New', 12), height=15, width=45)
text.pack(pady=10, padx=10)

scroll = ttk.Scrollbar(LF2, orient=VERTICAL, command=text.yview)
scroll.place(x=402, y=10, height=275)
text.config(yscrollcommand=scroll.set)


def ShowData():
    data = readcsv()
    for row in data:
        text.insert(END,row)
        text.insert(END,'\n')
        
B3 = ttk.Button(LF1,text='Report', command=ShowData)
B3.pack(pady=10,padx=100,ipadx=20,ipady=20)

GUI.mainloop() 
