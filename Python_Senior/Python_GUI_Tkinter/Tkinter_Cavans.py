import tkinter as tk

window = tk.Tk()
window.title('My Carvans')
window.geometry('300x200')
# 定义一个画布
canvas = tk.Canvas(window, bg='green', height=100, width=200)
# 读取一个图片，Mac系统只能读取gif后缀图片
image_file = tk.PhotoImage(file='/Users/liyan/Desktop/PyCharm_Python/Python_Tutorial/Python_Senior/Python_GUI_Tkinter/inf.gif')
# 创造一个图片变量
# 里面的参数10,10就是图片放入画布的坐标，
# 而这里的anchor=nw则是把图片的左上角作为锚定点，在加上刚刚给的坐标位置，即可将图片位置确定。
# 最后一个参数的意思大家应该都知道，就是将刚刚存入的图片变量，赋值给image。
image = canvas.create_image(10, 10, anchor='nw', image=image_file)
x0, y0, x1, y1= 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1) # 创建一条直线
oval = canvas.create_oval(x0, y0, x1, y1, fill='red') # 创建一个圆，填充色为红色
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180) # 创建一个角度从0到180的扇形
rect = canvas.create_rectangle(100, 30, 100+20, 30+20) # 创建一个矩形
canvas.pack()

# 定义每点击一次按钮正方形向下移动两个单位操作
def moveit():
    canvas.move(rect, 0, 2)

b = tk.Button(window, text='move', command=moveit).pack()


window.mainloop()