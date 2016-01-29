from Tkinter  import *
def close_window(root):
    root.destroy()
    
window = Tk()
window.geometry("800x400")    
window.title("Data Masker")
frame=Frame(window)
frame.grid()
label=Label(frame,text="Data Masker : Demo Version 1.0")
label.grid()
label2=Label(frame,text="Data Masker : Demo Version 2.0")
label2.pack()
label3=Label(frame,text="Data Masker : Demo Version 3.0")
label3.grid(column=2)
button =Button(frame, text="EXIT",command = close_window)
button.grid()
height = 2
width = 2
"""
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Entry(root, text="")
        b.grid(row=i, column=j)
"""
window.mainloop()
