#本程序作者：时金韬 版权所有（2024.05.03 22:28）

#导入库，设置根窗口模式
import tkinter as tk
import os
root=tk.Tk()
root.title('第三方库管理器GUI版')
root.geometry('300x150+500+250')
root.wm_resizable(0,0)

#定义Button的回调函数
def install():
    name1=e1.get()
    os.system(f'pip install {name1}')
def uninstall():
    name2=e1.get()
    os.system(f'pip uninstall  {name2}')
def clear():
    e1.delete(0,tk.END)

#对Lable,Button进行定义
l1=tk.Label(root,text='请输入要处理的库:',font=('UTF-8',12),width=20,height=1)
e1=tk.Entry(root,font=('UTF-8',12))
b1=tk.Button(root,text='安装',command=install)
b2=tk.Button(root,text='卸载',command=uninstall)
b3=tk.Button(root,text='清除',command=clear)

#将Lable和Button放入根窗口
l1.pack()
e1.pack()
b1.pack()
b2.pack()
b3.pack()

#根窗口保持
root.mainloop()