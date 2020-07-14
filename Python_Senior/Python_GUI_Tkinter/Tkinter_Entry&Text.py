import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('300x200')
e = tk.Entry(window, show = None) # show = None：输入字符可见， show = '*':
e.pack()

# 在光标处插入entry输入框的数据
def insert_point():
    var = e.get()
    t.insert('insert', var)

# 在文本末尾插入entry输入框的数据
def insert_end():
    var = e.get()
    t.insert('end', var)
b1 = tk.Button(window, text = 'insert point', width = 15, height = 2, command = insert_point)
b1.pack()
b2 = tk.Button(window, text = 'insert end', width = 15, height = 2,command = insert_end)
b2.pack()

t = tk.Text(window, height = 5) # height定义文本框有多少行
t.pack()

window.mainloop()