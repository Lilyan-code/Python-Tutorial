import tkinter as tk

window = tk.Tk()
window.title('My MenuBar')
window.geometry('200x200')

l = tk.Label(window, text='', bg='red')
l.pack()
counter = 0

# 功能：每点击一次'New''Open''Save'就将counter+1，然后设置到Label上
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter+=1

# 定义一个MenuBar，在窗口上方
menubar = tk.Menu(window)
# 定义一个空的菜单栏单元
filemenu = tk.Menu(menubar, tearoff=0)
# 将定义的菜单栏单元命名为File
menubar.add_cascade(label='File', menu=filemenu)
# 给菜单栏添加小的菜单，就是我们平时窗口操作的下拉菜单，每一个小的菜单对应一个功能。
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator() # 加一条分割线
filemenu.add_command(label='Exit', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu, underline=0) # 在filemenu加入一个小菜单
submenu.add_command(label="Submenu1", command=do_job)

window.config(menu=menubar)

window.mainloop()
