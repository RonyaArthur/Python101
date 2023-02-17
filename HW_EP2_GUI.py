from tkinter import *
from tkinter import ttk # theme og tk
from PIL import Image, ImageTk
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

###################### DATA ######################

L1 = Label(GUI,text='วันที่',font=('Angsana New',22,'bold'),fg='black')
L1.place(x=60,y=100)
E1 = ttk.Entry(GUI,width=3,font=('Angsana New',20),validate='key', validatecommand=(GUI.register(validate_input), '%P'))
E1.place(x=110,y=101)

L2 = Label(GUI,text='เดือน',font=('Angsana New',22,'bold'),fg='black')
L2.place(x=148,y=100)
C1 = ttk.Combobox(GUI,width=6,font=('Angsana New',20),value=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"])
C1.place(x=200,y=101)

L3 = Label(GUI,text='ปี',font=('Angsana New',22,'bold'),fg='black')
L3.place(x=285,y=100)
C2 = ttk.Combobox(GUI,width=6,font=('Angsana New',20),value=["2022","2023","2024"])
C2.place(x=310,y=101)

L4 = Label(GUI,text='ประเภท',font=('Angsana New',22,'bold'),fg='black')
L4.place(x=60,y=160)
C3 = ttk.Combobox(GUI,width=20,font=('Angsana New',20),value=["อาหาร","ช้อปปิ้ง","ของใช้ประจำวัน","ครอบครัว","อื่น"],justify='center')
C3.place(x=155,y=161)

L5 = Label(GUI,text='รายการ',font=('Angsana New',22,'bold'),fg='black')
L5.place(x=60,y=220)
E2 = ttk.Entry(GUI,width=20,font=('Angsana New',20), justify='center')
E2.place(x=155,y=221)


L6 = Label(GUI,text='จำนวนเงิน',font=('Angsana New',22,'bold'),fg='black')
L6.place(x=60,y=280)
E3 = ttk.Entry(GUI,width=20,font=('Angsana New',20), justify='center')
E3.place(x=155,y=281)
L7 = Label(GUI,text='บาท',font=('Angsana New',22,'bold'),fg='black')
L7.place(x=360,y=280)

###################### SAVE ######################

def Button():
    text = 'บันทึกสำเร็จ'
    messagebox.showinfo('Record',text)

style = ttk.Style()
style.configure('Custom.TButton', font=('Angsana New',20,'bold'))

B1 = ttk.Button(text='SAVE',command=Button,width=10,style='Custom.TButton')
B1.place(x=180,y=340)


img = Image.open("C:\00Ronnakorn\Training\Python\101\money.png")
img = img.resize((500, 500), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)

# Create a Label with the image
bg_label = Label(GUI, image=photoImg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

GUI.mainloop()

