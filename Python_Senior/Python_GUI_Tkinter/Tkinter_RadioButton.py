import tkinter as tk

window = tk.Tk()
window.title('My RadioButton')
window.geometry('400x400')

var = tk.StringVar()
l = tk.Label(window, text = 'empty', bg = 'red', font = ('Arial', 12), width = 25, height = 5)
l.pack()

def choose_button():
    l.config(text = 'you have choosen ' + var.get()) #config()给Label进行属性设置，这里获取当前选项的value进行绑定

# RadioButton中variable将所选中的value值绑定到var变量中，方便在点击后，给label进行绑定
r1 = tk.Radiobutton(window, text = 'Option A', variable = var, value = 'A', command = choose_button)
r1.pack()

r2 = tk.Radiobutton(window, text = 'Option B', variable = var, value = 'B', command = choose_button)
r2.pack()

r3 = tk.Radiobutton(window, text = 'Option C', variable = var, value = 'C', command = choose_button)
r3.pack()

window.mainloop()