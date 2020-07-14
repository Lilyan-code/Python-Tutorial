import tkinter as tk

window = tk.Tk()
window.title('My Frame')
window.geometry('200x200')
tk.Label(window, text='on the window').pack()

# 创建一个主框架
frm = tk.Frame(window)
frm.pack()
# 基于frm框架创建一个左边的子框架
frm_l = tk.Frame(frm)
# 基于frm框架创建一个右边的子框架
frm_r = tk.Frame(frm)
frm_l.pack(side='left') # pack中的side方法是将frm_l,frm_r两个子框架按照左或右的方向添加到frm上
frm_r.pack(side='right')

# 这里的三个label就是在我们创建的frame上定义的label部件，还是以容器理解，就是容器上贴了标签，
# 来指明这个是什么，解释这个容器。
tk.Label(frm_l, text='on the frm_l1').pack()
tk.Label(frm_l, text='on the frm_l2').pack()
tk.Label(frm_r, text='on the frm_r1').pack()
window.mainloop()