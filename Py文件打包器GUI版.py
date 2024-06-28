#本程序作者：时金韬 版权所有（2024.05.03 16:45）

#导入库，创建根窗口
import tkinter as tk
import os
root=tk.Tk()
root.title('Py文件打包器GUI版')
root.geometry('410x300')
root.wm_resizable(0,0)

#对Lable和Button的行为进行定义
def install():
    os.system('pip install pyinstaller')
def makebag():
    path1=e1.get()
    path2=e2.get()
    os.system(f'pyinstaller -F -w {path1} --workpath={path2} -specpath={path2}{path1} --distpath="{path2}"')
def clear_entry():
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)
def uninstall():
    os.system('pip uninstall pyinstaller')
        
#定义Lable和Entry，用于输入路径
l1=tk.Label(root,text='打包文件路径:',font=('UTF-8',12),width=20,height=1)
l2=tk.Label(root,text='文件输出路径:',font=('UTF-8',12),width=20,height=1)
lk=tk.Label(root,text='',font=('UTF-8',12),width=5,height=1)
e1=tk.Entry(root,font=('UTF-8',12))
e2=tk.Entry(root,font=('UTF-8',12))
b1=tk.Button(root,text='开始打包',command=makebag)
b2=tk.Button(root,text='点我安装打包组件',command=install)
b3=tk.Button(root,text='点我卸载打包组件',command=uninstall)
buclear=tk.Button(root,text='清除输入框',command=clear_entry)
sm=str("打包组件:Pyinstaller打包组件.\n注意:build文件夹和EXE在你输入的路径,spec文件在打包器根目录.")
lsm=tk.Label(root,text=sm,height=3)

#把Lable和Entry放入根窗口
l1.pack()
e1.pack()
l2.pack()
e2.pack()
lk.pack()
b1.pack()
buclear.pack()
b2.pack()
b3.pack()
lsm.pack()

#根窗口保持
root.mainloop()