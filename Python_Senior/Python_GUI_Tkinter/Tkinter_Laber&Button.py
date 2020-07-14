import tkinter as tk

window = tk.Tk() # 创建一个窗口对象
window.title('my first window') #给窗口命名
window.geometry('200x100') #定义窗口的长宽，geometry方法中传入字符串参数，字符串中应为长x宽（Note:x是小写字母x)

# Label(master = None, cnf = {}, **kw), kw参数是类似dict一样接收label组件定义的键值对
#l = tk.Label(window, text='successful! created new Label', bg='green', font=('Arial', 12), width=25, height=4)
var = tk.StringVar() #将label中的文本动态化设置，可以利用var.set()方法设置textvariable
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=25, height=4)
l.pack() #将定义好的label添加到window上

is_Hidden = False # 设置一个flag变量，用来判断现在窗口的label是显示的还是未显示的
def hidden_me():
    global is_Hidden
    if is_Hidden == False:
        is_Hidden = True
        var.set('click me and hidden')
    else:
        is_Hidden = False
        var.set('')

var1 = tk.StringVar()
var1.set('hidden')
#Button(master, option = value, ..), command是点击后发生什么效果的函数
b = tk.Button(window, textvariable = var1, width = 12, height = 2, command = hidden_me)
b.pack()  # 将button显示在窗口中

window.mainloop()  #mainloop实际上是使用while循环实现的，因为窗口的内容是会动态变化的
