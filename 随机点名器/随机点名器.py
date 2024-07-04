'''
这是一个随机点名程序.
先读取csv文件(文件名必须为NameList.csv!),
再利用random模块随机抽取,
最后用tkinter模块展示结果.

作者:时金韬(GitHub:不曾想过) 2024.7.4
'''
import random
import tkinter as tk
import csv

root = tk.Tk()
root.title("随机点名器")
root.geometry("500x200")
var = tk.StringVar()

def read():
    global column
    with open("NameList.csv") as n:
        reader = csv.reader(n)
        column = [row[0] for row in reader]

def choiceName():
    t = random.choice(column)
    var.set(t)

l1 = tk.Label(root,textvariable=var,font=('黑体',100),width=300,height=150)
b1 = tk.Button(root,text='抽取',command=choiceName)
b2 = tk.Button(root,text="读取文件",command=read)
b1.pack()
b2.pack()
l1.pack()

root.mainloop()