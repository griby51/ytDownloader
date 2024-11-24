from pytubefix import Playlist, YouTube
from tkinter import *

#comment this code 
window = Tk()


window.title("Youtube Downloader")

window.geometry('720x200')
window.minsize(720, 100)
window.config(bg="#383838")

frame0 = Frame(window, bg="#383838")

frame = Frame(frame0, bg="#383838")

label_dlVideo = Label(frame, text="Link :", font=("Arial", 15), bg="#383838", fg="white")
label_dlVideo.pack(padx=25)

link = Entry(frame, bg="#121212", fg="white", border=0, font=("Arial", 15), insertbackground="white")
link.pack(fill=X, padx=25)

dlButton = Button(frame, text="Download", command = lambda: dlVideo(link.get()), bg="#2C2C2C", fg="white", border=0, activebackground="#1E1E1E", font=("Arial", 15), activeforeground="white")
dlButton.pack(padx=25, pady=10, fill=X)

frame.grid(row=0, column=0)

frame1 = Frame(frame0, bg="#383838")

label_dlPlaylist = Label(frame1, text="Playlist link :", font=("Arial", 15), bg="#383838", fg="white")
label_dlPlaylist.pack(padx=25)

link = Entry(frame1, bg="#121212", fg="white", border=0, font=("Arial", 15), insertbackground="white")
link.pack(fill=X, padx=25)

dlButton = Button(frame1, text="Download", command = lambda: dlPlaylist(link.get()), bg="#2C2C2C", fg="white", border=0, activebackground="#1E1E1E", font=("Arial", 15), activeforeground="white")
dlButton.pack(padx=25, pady=10, fill=X)

frame1.grid(row=0, column=3)

frame0.pack(expand=True)

progression_label = Label(window, text="", bg="#383838", fg="white", font=("Arial", 15))
progression_label.pack(pady=10, side=BOTTOM)
def dlVideo(video_url):
    yt = YouTube(video_url)
    video = yt.streams.get_audio_only()
    video.download("music")

    progression_label["text"] = "Done"


def dlPlaylist(playlist_url):
    pl = Playlist(playlist_url)

    pl_lenght = len(pl.video_urls)
    i = 1
    for video_url in pl.video_urls:

        yt = YouTube(video_url)
        video = yt.streams.get_audio_only()
        video.download("music")
        print(i, "of", pl_lenght, " : ", video.title)
        progression_label["text"] = f"{i} of {pl_lenght}"
        i += 1
        if i == pl_lenght:
            progression_label["text"] = "Done"

window.mainloop()