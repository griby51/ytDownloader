import tkinter as tk
from pytubefix import Playlist, YouTube
import main as ytd

window = tk.Tk()
window.title("Youtube Downloader")
window.geometry('720x360')
window.minsize(720, 360)
window.config(bg="#383838")
isPlaylist = tk.BooleanVar()
onlyAudio = tk.BooleanVar()

titleLabel = tk.Label(window, text="Youtube Downloader", font=("Arial", 20), bg="#383838", fg="white")
linkLabel = tk.Label(window, text="Enter link :", font=("Arial", 15), bg="#383838", fg="white")
linkEntry = tk.Entry(window, bg="#121212", fg="white", border=0, font=("Arial", 15), insertbackground="white")
dlButton = tk.Button(window, text="Download", fg="white", bg="#2C2C2C", border=0, activebackground="#1E1E1E", font=("Arial", 15), activeforeground="white")

playlistCheckButton = tk.Checkbutton(
    window,bg="#383838",
    fg="white",
    activebackground="#383838",
    selectcolor="#383838",
    text="Playlist",
    activeforeground="white",
    font=("Arial", 15),
    variable=isPlaylist,
    onvalue=True,
    offvalue=False
    )

onlyAudioCheckButton =tk.Checkbutton(
    window,bg="#383838",
    fg="white",
    activebackground="#383838",
    selectcolor="#383838",
    text="Only Audio",
    activeforeground="white",
    font=("Arial", 15),
    variable=onlyAudio,
    onvalue=True,
    offvalue=False
    )

#progress bar


#place title at top center
titleLabel.place(relx=0.5, rely=0.1, anchor="center")

#place link label at the left
linkLabel.place(relx=0.1, rely=0.3, anchor="w")

#place link entry at the center and fill X
linkEntry.place(relx=0.1, rely=0.4, anchor="w", relwidth=0.8)

playlistCheckButton.place(relx=0.1, rely=0.5, anchor="w")
onlyAudioCheckButton.place(relx=0.3, rely=0.5, anchor="w")

#place download button at the center and fill X
dlButton.place(relx=0.5, rely=0.6, anchor="center", relwidth=0.8)




window.mainloop()