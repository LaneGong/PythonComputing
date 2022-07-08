import tkinter
import tkinter.messagebox
from task4_classes import *


def init(windows):#初始化界面，用户登陆
    windows.title('订餐系统')
    windows.geometry('240x240')
    lb1=tkinter.Label(windows,text='请输入用户名进入点餐系统',bg='#d3fbfb',fg='red',font=('',15), width=100,height=1)
    lb1.pack()
    labeluser=tkinter.Label(windows,text='User Name',font=('',15),width=80)
    labeluser.place(x=80,y=40,width=80,height=20)
    varname=tkinter.StringVar(windows,value='')
    entryname=tkinter.Entry(windows,width=80,textvariable=varname)
    entryname.place(x=80,y=70,width=80,height=30)
    entrybutton=tkinter.Button(windows,text='Login',command=lambda :login(entryname,windows))
    entrybutton.place(x=80,y=110,width=80,height=20)

def login(entryname,windows):
    name=entryname.get()
    if not name:
        tkinter.messagebox.showerror('警告',message='用户名不能为空！')
    else:
        cus=Customer()
        cus.name=name
        index(windows,cus)


def index(windows,user):
    indexpage=tkinter.Toplevel(windows,width=500,height=550)
    indexpage.title('Hi '+user.name+'!Weclome to order!')
    lb1 = tkinter.Label(indexpage, text='欢迎进入点餐系统！', bg='#d3fbfb', fg='red', font=('', 32), width=25, height=2)
    lb1.place(x=0,y=0)
    lb2 = tkinter.Label(indexpage, text='当前可下单商户', bg='#FFFF00', font=('', 20), width=12, height=1)
    lb2.place(x=0,y=83)
    empl1=tkinter.Button(indexpage,text='KFC',command=lambda :order_process(1,user,indexpage),width=15,height=3)
    empl1.place(x=0,y=120)
    empl2 = tkinter.Button(indexpage, text='Mcdonald\'s', command=lambda: order_process(2, user,indexpage), width=15, height=3)
    empl2.place(x=0, y=180)
    empl3 = tkinter.Button(indexpage, text='BurgerKing', command=lambda: order_process(3, user,indexpage), width=15, height=3)
    empl3.place(x=0, y=240)
    lb3 = tkinter.Label(indexpage, text='MENU', bg='#FFFF00', font=('', 20), width=12, height=1)
    lb3.place(x=260, y=83)

def order_process(type,user,indexpage):
    order1=Launch()
    order1.cust.name=user.name
    if type==1:
        var1=tkinter.IntVar()
        var2=tkinter.IntVar()
        var3=tkinter.IntVar()
        ch1=tkinter.Checkbutton(indexpage, text='KFC1             ', variable=var1, onvalue=1, offvalue=0)
        ch2=tkinter.Checkbutton(indexpage, text='KFC2             ', variable=var2, onvalue=1, offvalue=0)
        ch3=tkinter.Checkbutton(indexpage, text='KFC3             ', variable=var3, onvalue=1, offvalue=0)
        ch1.place(x=260,y=130)
        ch2.place(x=260,y=190)
        ch3.place(x=260,y=250)
        order1.empl.name='KFC'
        btn=tkinter.Button(indexpage, text="OK", command=lambda :orders(order1,var1,var2,var3),width=15, height=1)
        btn.place(x=150,y=320)
        btn2 = tkinter.Button(indexpage, text='打印订单', command=lambda: printfood(indexpage, order1), width=15, height=1)
        btn2.place(x=150, y=360)
    elif type==2:
        var1 = tkinter.IntVar()
        var2 = tkinter.IntVar()
        var3 = tkinter.IntVar()
        ch1 = tkinter.Checkbutton(indexpage, text='Mcdonald\'s 1', variable=var1, onvalue=1, offvalue=0)
        ch2 = tkinter.Checkbutton(indexpage, text='Mcdonald\'s 2', variable=var2, onvalue=1, offvalue=0)
        ch3 = tkinter.Checkbutton(indexpage, text='Mcdonald\'s 3', variable=var3, onvalue=1, offvalue=0)
        ch1.place(x=260, y=130)
        ch2.place(x=260, y=190)
        ch3.place(x=260, y=250)
        order1.empl.name = 'Mcdonald\'s'
        btn = tkinter.Button(indexpage, text="OK", command=lambda :orders(order1,var1,var2,var3), width=15, height=1)
        btn.place(x=150, y=320)
        btn2 = tkinter.Button(indexpage, text='打印订单', command=lambda: printfood(indexpage, order1), width=15, height=1)
        btn2.place(x=150, y=360)
    else:
        var1 = tkinter.IntVar()
        var2 = tkinter.IntVar()
        var3 = tkinter.IntVar()
        ch1= tkinter.Checkbutton(indexpage, text='BurgerKing 1', variable=var1, onvalue=1, offvalue=0)
        ch2= tkinter.Checkbutton(indexpage, text='BurgerKing 2', variable=var2, onvalue=1, offvalue=0)
        ch3= tkinter.Checkbutton(indexpage, text='BurgerKing 3', variable=var3, onvalue=1, offvalue=0)
        ch1.place(x=260, y=130)
        ch2.place(x=260, y=190)
        ch3.place(x=260, y=250)
        order1.empl.name = 'BurgerKing'
        btn = tkinter.Button(indexpage, text="OK", command=lambda :orders(order1,var1,var2,var3), width=15, height=1)
        btn.place(x=150, y=320)
        btn2=tkinter.Button(indexpage,text='打印订单',command=lambda :printfood(indexpage,order1), width=15, height=1)
        btn2.place(x=150,y=360)

def orders(order1,var1,var2,var3):
    if var1.get()==1:
        food=order1.empl.name+' 1'
        order1.order(food)
    if var2.get()==1:
        food=order1.empl.name + ' 2'
        order1.order(food)
    if var3.get()==1:
        food = order1.empl.name + ' 3'
        order1.order(food)

def printfood(indexpage,order1):
    txt=tkinter.Text(indexpage)
    txt.place(x=0,y=400)
    message='Hi '+order1.cust.name+'~\n您的订单为:'
    txt.insert('end',message)
    order1.result(txt)

def runSystem():
    windows = tkinter.Tk()
    init(windows)
    windows.mainloop()