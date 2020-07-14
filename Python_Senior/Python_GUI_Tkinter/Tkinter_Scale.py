import tkinter as tk

window = tk.Tk()
window.title('My Scale')
window.geometry('300x300')

l = tk.Label(window, bg = 'blue', width = 20, text = 'empty')
l.pack()

# 这里参数v是用来记录滚动条定位的数据（滑动到哪里了）
def job(v):
    l.config(text = 'you have choosen ' + v)

# 参数解释：
# from_ = 1, to = 20:从1到20的意思，就是滚动条的起始刻度到终止刻度
# orient = tk.HORIZONAL是设置滚动条的方向，是纵向放，还是横向放
# length是指整个滚动条在window上的长度（以px像素为单位）
# resolution = 0.01是设置滚动条的精度，移动一步按照两位小数来计算
# showvalue = 1:表示滚动条的游标cur上方是否会显示当前选中的滑动值
# tkinterval = 4:设置滚动条下方的坐标间隔，这里按照每4个单位来计算
s = tk.Scale(window, label = 'push me', from_ = 1, to = 20, orient = tk.HORIZONTAL,
             length = 200, showvalue = 1, tickinterval = 4, resolution = 0.01, command = job)
s.pack()

window.mainloop()