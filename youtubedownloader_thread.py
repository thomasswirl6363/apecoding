from pytube import YouTube
import tkinter as tk
window=tk.Tk()
import threading

window.title("Youtube Downloader")
window.geometry("500x150")
window.resizable(False, False)


progress=0


def showProgress(stream,chunk,bytes_remaining):
    size=stream.filesize
    global progress
    preProgress=progress
    currentProgress=(size-bytes_remaining)*100//size
    progress=currentProgress
    
    if progress==100:
        print("下載完成")
        return
    elif preProgress!=progress:
        scale.set(progress)
        window.update()
        print("目前進度"+str(progress)+"%")
def onClick(): 
    
    global var
    var.set(entry.get())
    
    button.config(state=tk.DISABLED)
    label.config(text="正在下載中")
    try:
        yt=YouTube(var.get(), on_progress_callback=showProgress)
        stream=yt.streams.first()
        stream.download("youtube", yt.title)
        if onlyMusic.get():
            stream=yt.streams.filter(only_audio=True).first()
        else:
            stream=yt.streams.first()
        stream.download("youtube", yt.title)
    except:
        print("下載失敗")
        button.config(state=tk.NORMAL)
def th():
    threading.Thread(target=onClick).start()
    
label=tk.Label(window, text="請輸入 Youtube 網址")
label.pack()

var=tk.StringVar()
entry=tk.Entry(window, width=50)
entry.pack()
onlyMusic=tk.BooleanVar()
check=tk.Checkbutton(window, text="只有音樂", variable=onlyMusic, onvalue=True, offvalue=False)

check.pack()

button=tk.Button(window, text="下載", command=th)
button.pack()

scale=tk.Scale(window, label="進度條", from_=0, to =100
               ,orient=tk.HORIZONTAL, length=200, showvalue=False, tickinterval=0)
scale.pack()

window.mainloop()