import tkinter as tk

window = tk.Tk()
window.title('My CheckBox')
window.geometry('300x300')

l = tk.Label(window, bg = 'red', width = 20, text = 'empty')
l.pack()

# 通过判断每个复选框是否被选择来进行判断。再将Label显示内容进行替换
def job():
    if (var1.get() == 1) and (var2.get() == 0) and (var3.get() == 0):
        l.config(text = 'I love only C++')
    elif (var1.get() == 0) and (var2.get() == 1) and (var3.get() == 0):
        l.config(text = 'I love only Java')
    elif (var1.get() == 0) and (var2.get() == 0) and (var3.get() == 1):
        l.config(text = 'I love only Python')
    elif (var1.get() == 1) and (var2.get() == 1) and (var3.get() == 0):
        l.config(text = 'I love C++ and Java')
    elif (var1.get() == 1) and (var2.get() == 0) and (var3.get() == 1):
        l.config(text = 'I love C++ and Python')
    elif (var1.get() == 0) and (var2.get() == 1) and (var3.get() == 1):
        l.config(text = 'I love Java and Python')
    elif (var1.get() == 1) and (var2.get() == 1) and (var3.get() == 1):
        l.config(text = 'I love C++ and Java and Python')
    else :
        l.config(text = 'I love all lanuage')

var1 = tk.IntVar()
# 参数解释： variable:表示将var1变量绑定到cb1上
# 参数onvalue和前面讲的部件radiobutton中的value相似， 当我们选中了这个checkbutton，
# onvalue的值1就会放入到var1中， 然后var1将其赋值给参数variable，offvalue用法相似，
# 但是offvalue是在没有选中这个checkbutton时，offvalue的值1放入var1，然后赋值给参数variable
# 这是创建一个checkbutton部件，以此类推，可以创建多个checkbutton
cb1 = tk.Checkbutton(window, text = 'C++', variable = var1, onvalue = 1, offvalue = 0, command = job)
var2 = tk.IntVar()
cb2 = tk.Checkbutton(window, text = 'Java', variable = var2, onvalue = 1, offvalue = 0, command = job)
var3 = tk.IntVar()
cb3 = tk.Checkbutton(window, text = 'Python', variable = var3, onvalue = 1, offvalue = 0, command = job)
cb1.pack()
cb2.pack()
cb3.pack()

window.mainloop()