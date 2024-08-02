'''
This file is licensed under the Eclipse Public License 2.0 (EPL-2.0).
You can find a copy of the license at https://www.eclipse.org/legal/epl-2.0/

作者:sjt-2024 版权所有
Github: https://github.com/sjt-2024/
日期:2024-08-02

Author: sjt-2024
Copyright Holder: sjt-2024
Github: https://github.com/sjt-2024/
Date: 2024-08-02
'''

# 导入库
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox as msgbox

# 创建窗口
root = ttk.Window(themename="cosmo")  # 选择一个主题
root.title("歌曲宝专用爬歌词工具 v1.5")
root.resizable(False, False)

# 请求头(Referer要根据实际情况修改)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.gequbao.com/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br'
}

# 请求函数
def get_lyrics():
    global lyrics
    global targets
    global music_name
    global music_name_tag
    global res_status
    url = f"https://www.gequbao.com/music/{text.get('1.0', 'end-1c')}".strip()  # 获取输入的链接并清理
    try:
        res = requests.get(url, headers=headers, timeout=10, allow_redirects=True)  # 允许重定向
        res.raise_for_status()
    except requests.Timeout:
        output.insert(tk.END,"请求超时，请重试")
        return
    except requests.RequestException as e:
        output.insert(tk.END,f"请求错误: {e}\n")
        return

    soup = BeautifulSoup(res.text, 'html.parser')
    targets = soup.find('div', class_='content-lrc mt-1')  # 找到歌词所在的div
    
    # 处理非纯数字歌曲ID报错
    try:
        music_name_tag = soup.find('span', class_="form-control bg-light overflow-hidden")
        if music_name_tag: # 去除歌曲名末尾的".mp3"
            music_name = music_name_tag.text.strip()
            music_name = music_name.rstrip(".mp3")
        else:
            music_name = "未知歌曲名"
    except AttributeError as e:
        music_name = "未知歌曲名"
        output.insert(tk.END,f"获取歌曲名时发生错误: {e}")
        return
    else:
        # 找到歌曲名
        music_name = music_name.rstrip(".mp3")
        if targets:
            lyrics = music_name + '\n' +'\n'.join(line.strip() for line in targets.stripped_strings if line.strip())
            output.delete(1.0, tk.END)  # 清空文本框
            output.insert(tk.END, lyrics)  # 插入新文本
        else:
            output.delete(1.0, tk.END)  # 清空文本框
            output.insert(1.0, "未找到歌词")

# 创建文本框
label = ttk.Label(root, text="请输入歌曲宝的歌曲ID=======>>\n\n格式:*https://www.gequbao.com/music/*歌曲ID\n用*包裹的部分是缺省的,请勿输入")
label.grid(row=0, column=0, padx=10, pady=10)
text = ttk.Text(root, width=50, height=5)
text.grid(row=0, column=1, padx=10, pady=10)
reminder = ttk.Label(root, text="下面是爬取结果↓")
reminder.grid(row=1, column=0, padx=5, pady=10)

# 输出框
output = ttk.Text(root, width=90, height=20)
output.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# 添加滚动条
scrollbar = ttk.Scrollbar(root, command=output.yview)
scrollbar.grid(row=2, column=2, sticky='ns')
output.config(yscrollcommand=scrollbar.set)

# 按钮
but = ttk.Button(root, text="开始爬取", command=get_lyrics)
but.grid(row=1, column=1, padx=10, pady=10)

# 选择保存路径
def select_path():
    path = filedialog.asksaveasfilename(title="保存歌词文件", filetypes=[("文本文件", "*.txt")],defaultextension=".txt")
    if path:
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(output.get("1.0", "end-1c").strip())
        except Exception as e:
            msgbox.show_error(title="保存文件错误", message=f"保存文件错误: {e}")
    else:
        msgbox.show_info(title="提示", message="未选择保存路径")

# 保存文件按钮
save_Button = ttk.Button(root, text="保存文件", command=select_path)
save_Button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# 运行主程序
root.mainloop()