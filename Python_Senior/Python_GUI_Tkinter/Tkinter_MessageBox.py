import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('My MessageBox')
window.geometry('200x200')

def job():
    # tk.messagebox.showinfo(title='Hi', message='hahahaha')   # return 'ok'
    # tk.messagebox.showwarning(title='Hi', message='nononono')   # return 'ok' 警告框
    # tk.messagebox.showerror(title='Hi', message='No!! never')   # return 'ok' 错误框
    # print(tk.messagebox.askquestion(title='Hi', message='hahahaha'))   # return 'yes' , 'no'
     print(tk.messagebox.askyesno(title='Hi', message='hahahaha'))   # return True, False
    # print(tk.messagebox.asktrycancel(title='Hi', message='hahahaha'))  # return True, False
    # print(tk.messagebox.askokcancel(title='Hi', message='hahahaha'))  # return True, False
    # print(tk.messagebox.askyesnocancel(title="Hi", message="haha"))  # return, True, False, None

b = tk.Button(window, text = 'click me', bg = 'yellow', command = job)
b.pack()

window.mainloop()