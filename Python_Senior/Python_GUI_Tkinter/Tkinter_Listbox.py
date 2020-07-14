import tkinter as tk

window = tk.Tk()
window.title('My Listbox')
window.geometry('300x200')

var1 = tk.StringVar()
l = tk.Label(window, textvariable = var1, bg = 'yellow', font=('Arial', 12), width=25, height=4)
l.pack()

def print_selection():
    tmp = lb.get(lb.curselection()) #curselection()表示的是获取当前列表所选中的
    var1.set(tmp) # 将当前所选中的listbox的value设置到Lable上。

b = tk.Button(window, text = 'print list selection', width = 12, height = 2, command = print_selection)
b.pack()
var2 = tk.StringVar()
var2.set(('first', 'second', 'third', 'fourth'))
lb = tk.Listbox(window, listvariable = var2) # 初始化listbox时，将var2赋值给lb初始化
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)

# 还可以使用insert(index, value)形式，按照list的下标插入value
# lb.insert(1, 'one')
# 使用delete(index)形式，删除list中index的元素
lb.pack()

window.mainloop()
