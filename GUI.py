import os
import tkinter
import module1
import module2
from tkinter import *
from tkinter import messagebox


def result():
    in_file = u1.get()
    out_file = u2.get()
    pro = u3.get()
    if pro == '':
        module2.yq_seq(in_file, out_file)
    else:
        module1.yq_select(in_file, out_file, pro)
    messagebox.showinfo("生成结果", "成功保存至" + os.path.abspath(out_file))


# 创建窗口：实例化一个窗口
root = tkinter.Tk()
# 设置窗口大小，位置
root.geometry("600x300+374+182")
# 设置窗口标题
root.title("GUI可视化界面")
# 绑定对象到Entry
u1 = StringVar()
u2 = StringVar()
u3 = StringVar()
# 添加标签、输入框并分别定位
label1 = Label(root, text="输入文件", font=("宋体", 13)).grid(row=0, column=0)
entry1 = Entry(root, font=("宋体", 13), bd="5", width="35", textvariable=u1).grid(row=0, column=1)
label2 = Label(root, text="输出文件", font=("宋体", 13)).grid(row=1, column=0)
entry2 = Entry(root, font=("宋体", 13), bd="5", width="35", textvariable=u2).grid(row=1, column=1)
label3 = Label(root, text="省份", font=("宋体", 13)).grid(row=2, column=0)
entry3 = Entry(root, font=("宋体", 13), bd="5", width="35", textvariable=u3).grid(row=2, column=1)

# 添加按钮
button1 = Button(root, text="生成", font=("宋体", 13), activebackground="blue", command=result).grid(row=0, column=2)
button2 = Button(root, text='清空', font=("宋体", 13), activebackground="blue")


# 清空回调函数
def clear(e):  # 创建函数，触发事件时被调用
    u1.set('')
    u2.set('')
    u3.set('')


button2.bind('<Button-1>', clear)  # 绑定事件
button2.grid(row=1, column=2)

# 显示窗口
root.mainloop()
