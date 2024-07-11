'''
这是一个随机点名程序.
先读取csv文件,
再利用random模块随机抽取,
最后用tkinter模块展示结果.

作者:时金韬(GitHub:不曾想过) 2024.7.4
'''
import random
import tkinter as tk
import csv
from tkinter import messagebox as msg
from tkinter.filedialog import askopenfilename

root = tk.Tk()
root.title("随机点名器")
root.geometry("520x260")
root.wm_resizable(0,0)
var = tk.StringVar()


def read(): #读取
        global column
        global open_file
        open_file = askopenfilename(title="请选择文件",filetypes=[("csv文件","*.csv")])
        try:
            with open(open_file) as m:
                reader = csv.reader(m)
                column = [row[0] for row in reader]
        except FileNotFoundError:
            pass
def choiceName(): #抽取
    try:
        t = random.choice(column)
        var.set(t)
    except NameError:
        print(msg.showerror(title="错误",message="请先读取文件!"))
    except UnboundLocalError:
        pass

showLable = tk.Label(root,textvariable=var,font=('黑体',100),width=300,height=150)
choiceBut = tk.Button(root,text='抽取',command=choiceName)
readBut_tj = tk.Button(root,text="读取文件",command=read)

readBut_tj.pack()
choiceBut.pack()
showLable.pack()

root.mainloop()