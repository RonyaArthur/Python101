from tkinter import *
from tkinter import ttk # theme og tk
from tkinter import messagebox

GUI = Tk()      # นี้คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมรายจ่ายประจำวัน')    # นี้คือชื่อโปรแกรม
GUI.geometry('500x500')     # นี้คือขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมรายจ่ายประจำวัน',font=('Angsana New',32,'bold'),fg='blue')
L1.place(x=90,y=20)

##################################################
def validate_input(new_value):
    # Check if the new value has a length of 0 or 1, or if it is a valid integer with a length of 2
    return len(new_value) == 0 or len(new_value) == 1 or (new_value.isdigit() and len(new_value) == 2)

######################CSV##################################################################

import csv
def writecsv(datalist):
    with open('รายจ่ายประจำวัน.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']

def readcsv(): # fuction อ่านข้อมูลจาก csv file
    with open('รายจ่ายประจำวัน.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fw = file reader
        data = list(fr)
    return data

######################CSV#################################################################

###################### DATA ######################

L1 = Label(GUI,text='วันที่',font=('Angsana New',22,'bold'),fg='black')
L1.place(x=60,y=100)
v_data1 = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_data1,width=3,font=('Angsana New',20),validate='key', validatecommand=(GUI.register(validate_input), '%P'))
E1.place(x=110,y=101)

L2 = Label(GUI,text='เดือน',font=('Angsana New',22,'bold'),fg='black')
L2.place(x=148,y=100)
v_data2 = StringVar()
C1 = ttk.Combobox(GUI,textvariable=v_data2,width=6,font=('Angsana New',20),value=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"])
C1.place(x=200,y=101)

L3 = Label(GUI,text='ปี',font=('Angsana New',22,'bold'),fg='black')
L3.place(x=285,y=100)
v_data3 = StringVar()
C2 = ttk.Combobox(GUI,textvariable=v_data3,width=6,font=('Angsana New',20),value=["2022","2023","2024"])
C2.place(x=310,y=101)

L4 = Label(GUI,text='ประเภท',font=('Angsana New',22,'bold'),fg='black')
L4.place(x=60,y=160)
v_data4 = StringVar()
C3 = ttk.Combobox(GUI,textvariable=v_data4,width=20,font=('Angsana New',20),value=["อาหาร","ช้อปปิ้ง","ของใช้ประจำวัน","ครอบครัว","อื่น"],justify='center')
C3.place(x=155,y=161)

L5 = Label(GUI,text='รายการ',font=('Angsana New',22,'bold'),fg='black')
L5.place(x=60,y=220)
v_data5 = StringVar()
E2 = ttk.Entry(GUI,textvariable=v_data5,width=20,font=('Angsana New',20), justify='center')
E2.place(x=155,y=221)


L6 = Label(GUI,text='จำนวนเงิน',font=('Angsana New',22,'bold'),fg='black')
L6.place(x=60,y=280)
v_data6 = StringVar()
E3 = ttk.Entry(GUI,textvariable=v_data6,width=20,font=('Angsana New',20), justify='center')
E3.place(x=155,y=281)
L7 = Label(GUI,text='บาท',font=('Angsana New',22,'bold'),fg='black')
L7.place(x=360,y=280)

###################### SAVE ######################
from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data1 = v_data1.get() + v_data2.get() +v_data3.get() # ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    data2 = v_data4.get()
    data3 = v_data5.get()
    data4 = v_data6.get()
    text = [t,data1,data2,data3,data4]
    writecsv(text)
    v_data1.set('')
    v_data2.set('')
    v_data3.set('')
    v_data4.set('')
    v_data5.set('')
    v_data6.set('')
    textF = 'บันทึกสำเร็จ'
    messagebox.showinfo('Record',textF)

################################################################################################################


style = ttk.Style()
style.configure('Custom.TButton', font=('Angsana New',20,'bold'))

B1 = ttk.Button(text='SAVE',command=SaveData,width=10,style='Custom.TButton')
B1.place(x=180,y=340)

GUI.mainloop()

