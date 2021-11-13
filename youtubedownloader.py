from pytube import YouTube

progress=0

def showProgress(stream,chunk,bytes_remaining):
    size=streams.filesize
    global progress
    preProgress=progress
    currentProgress=(size-bytes_remaining)*100//size
    progress=currentProgress
    
    if progress==100:
        print("下載完成")
        return
    elif preProgress!=progress:
        print("目前進度"+str(progress)+"%")

yt=YouTube("https://www.youtube.com/watch?v=D48T0wNm96w", on_progress_callback=showProgress)

streams=yt.streams.filter(only_audio=True).first()

streams.download("youtube",yt.title+"only_audio")