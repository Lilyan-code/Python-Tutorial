import tkinter as tk

window = tk.Tk() # 创建一个窗口对象
window.title('my first window') #给窗口命名
window.geometry('200x100') #定义窗口的长宽，geometry方法中传入字符串参数，字符串中应为长x宽（Note:x是小写字母x)

# Label(master = None, cnf = {}, **kw), kw参数是类似dict一样接收label组件定义的键值对
#l = tk.Label(window, text='successful! created new Label', bg='green', font=('Arial', 12), width=25, height=4)
var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=25, height=4)
l.pack() #将定义好的label添加到window上

is_Hidden = False
def hidden():
    global is_Hidden
    if is_Hidden == False:
        is_Hidden = True
        var.set('click me and hidden')
    else:
        is_Hidden = False
        var.set('')


b = tk.Button(window, text = 'hidden label', width = 12, height = 2, command = hidden)
b.pack()

window.mainloop()  #mainloop实际上是使用while循环实现的，因为窗口的内容是会动态变化的
