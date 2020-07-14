import tkinter as tk

window = tk.Tk()
window.geometry('200x200')

# 使用pack(side = '')来放置组件的位置
'''
tk.Label(window, text='1').pack(side='top')
tk.Label(window, text='1').pack(side='bottom')
tk.Label(window, text='1').pack(side='left')
tk.Label(window, text='1').pack(side='right')
'''

# 使用grid进行位置摆放组件：padx：单元格左右间距 pdy：单元格上下间距
'''
for i in range(4):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)
'''
# 使用place进行位置摆放组件：anchor：锚点的位置nw：north west西北方向
tk.Label(window, text=1).place(x=20, y=10, anchor='nw')

window.mainloop()