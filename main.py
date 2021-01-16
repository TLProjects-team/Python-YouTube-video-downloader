from tkinter import *
import pytube
import os
def download():
    video_url = url.get()
    username = os.getenv('UserName')
    try:
        youtube = pytube.YouTube(video_url)
        video   = youtube.streams.first()
        percorso = "C:/Users/"+username+"/Desktop/Videos"
        video.download(str(percorso))
        notif.config(fg="green", text=f"Video salvato in {str(percorso)}")
    except Exception as e:
        print(e)
        notif.config(fg="red", text="ERRORE")

#Main Screen
master = Tk()
master.title("YT Downloader")

#Labels
Label(master, text="YouTube Downloader", fg="red", font=("Calibri",15)).grid(sticky=N,padx=100,row=0)
Label(master, text="Link del video:", font=("Calibri",12)).grid(sticky=N,row=1,pady=15)
notif = Label(master,font=("Calibri",12))
notif.grid(sticky=N,pady=1,row=4)
#vars
url = StringVar()
#entry
Entry(master,width=50,textvariable=url).grid(sticky=N,row=2)
#Button
Button(master,width=20,text="Download",font=("Calibri",12),command=download).grid(sticky=N,row=3,pady=15)

master.mainloop()