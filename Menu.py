import tkinter as tk

window=tk.Tk()

window.title("Menu")

window.geometry("500x500")

menuBar=tk.Menu(window)


fileMenu=tk.Menu(menuBar, tearoff=False)

fileMenu.add_command(label="開新遊戲")

fileMenu.add_command(label="作弊指令")

fileMenu.add_separator()

fileMenu.add_command(label="Exit")

menuBar.add_cascade(label="檔案", menu=fileMenu)

fileMenu2=tk.Menu(menuBar, tearoff=False)

fileMenu2.add_command(label="遊戲設定")

fileMenu2.add_command(label="畫面設定")

subMenu=tk.Menu(menuBar, tearoff=False)

subMenu.add_command(label="遊戲優化MAX")

subMenu.add_command(label="攻擊所有敵人")

fileMenu2.add_cascade(label="進階設定", menu=subMenu)

menuBar.add_cascade(label="選項", menu=fileMenu2)

window.config(menu=menuBar)

window.mainloop()