import tkinter as tk

window=tk.Tk()

window.title("RadioButton")

window.geometry("500x500")

string=tk.StringVar()

string.set("Pygame")

gender=tk.StringVar()

gender.set("男")


def selection():
    label.config(text="我是"+gender.get()+","+"我喜歡"+string.get())
    
    
label=tk.Label(window, bg="#f00", text="尚未選擇")                  
label.pack()

radio1=tk.Radiobutton(window, text="Python Minecraft", variable=string, value="Python Minecraft", command=selection)

radio1.pack()

radio2=tk.Radiobutton(window, text="Pygame", variable=string, value="Pygame", command=selection)

radio2.pack()

radio3=tk.Radiobutton(window, text="Tkinter", variable=string, value="Tkinter", command=selection)

radio3.pack()

radio4=tk.Radiobutton(window, text="男", variable=gender, value="男", command=selection)

radio4.pack()

radio5=tk.Radiobutton(window, text="女", variable=gender, value="女", command=selection)

radio5.pack()

selection()

window.mainloop()