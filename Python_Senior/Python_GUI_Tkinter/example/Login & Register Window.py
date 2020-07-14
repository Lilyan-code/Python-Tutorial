import tkinter as tk
import pickle
import tkinter.messagebox

window = tk.Tk()
window.title('Login & Register Window')
window.geometry('450x300')

# 创建一个画布，将图片嵌入在画布上，以左上角为原点，使用pack方法将画布置于窗口顶部
canvas = tk.Canvas(window, height = 200, width = 500)
image_file = tk.PhotoImage(file = 'welcome.gif')
image = canvas.create_image(0, 0, anchor = 'nw', image = image_file)
canvas.pack(side = 'top')

# 在window上设置两个label表示用户名和用户密码
tk.Label(window, text = 'User_name:').place(x = 50, y = 150)
tk.Label(window, text = 'User_password:').place(x = 50, y = 200)

# 设置两个输入框，用户名输入框默认设置root，然后输入框使用place在window上定位
var_name = tk.StringVar()
var_name.set('root')
entry_name = tk.Entry(window, textvariable = var_name)
entry_name.place(x = 170, y = 150)
var_pwd = tk.StringVar()
entry_pwd = tk.Entry(window, textvariable = var_pwd, show = '*')
entry_pwd.place(x = 170, y = 200)

# 定义了Login的一些操作，里面使用pyhton的pickle模块进行对文件的操作，用dict存储用户名密码
# 将dict序列化存储到data.pickle中，再判断用户名密码的时候使用pickle.load加载数据
def Login():
    user_name = var_name.get()
    user_pwd = var_pwd.get()
    try:
        with open ('data.pickle', 'rb') as f:
            user_info = pickle.load(f)
    except FileNotFoundError:
        with open('data.pickle', 'wb') as f:
            user_info = {'root': 'root'}
            pickle.dump(user_info, f)
    # 判断用户名是否注册，用户名对应的密码是否一致
    if user_name in user_info:
        if user_pwd == user_info[user_name]:
            tk.messagebox.showinfo(title = 'Welcome', message = 'Welcome to ' + user_name)
        else:
            tk.messagebox.showerror(title = 'Error', message = 'your password is wrong, try again')
    else:
        is_register = tk.messagebox.askyesno('Welcome', 'You have not register yet. Register today?')
        # 如果还没注册，就跳转窗口进行register
        if is_register:
            Register()
# 定义了Register的操作
def Register():
    # 用于处理Register的窗口中注册button的功能
    def register():
        # 获取输入密码和确认密码，进行逻辑判断
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('data.pickle', 'rb') as f:
            exist_usr_info = pickle.load(f)
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already register!')
        else:
            exist_usr_info[nn] = np
            with open('data.pickle', 'wb') as f:
                pickle.dump(exist_usr_info, f)
            tk.messagebox.showinfo('Welcome', 'You have successfully register!')
            window_sign_up.destroy()
    # 创建一个新的窗口用于Register使用
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Register Window')

    new_name = tk.StringVar()
    new_name.set('root')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y= 10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Register', command = register)
    btn_comfirm_sign_up.place(x=150, y=130)

# 设置两个button，一个用于login，一个用于register
button_login = tk.Button(window, text = 'login', command = Login)
button_login.place(x = 170, y = 250)
button_register = tk.Button(window, text = 'register', command = Register)
button_register.place(x = 270, y = 250)

window.mainloop()