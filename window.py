import tkinter as tk
from pytubefix import Playlist, YouTube
import threading

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

progressBarLabelVideo = tk.Label(window, text="", bg="#383838", fg="white", font=("Arial", 15))
progressBarLabelPlaylist = tk.Label(window, text="", bg="#383838", fg="white", font=("Arial", 15))

playlistCheckButton = tk.Checkbutton(
    window, bg="#383838", fg="white", activebackground="#383838",
    selectcolor="#383838", text="Playlist", activeforeground="white",
    font=("Arial", 15), variable=isPlaylist, onvalue=True, offvalue=False
)
onlyAudioCheckButton = tk.Checkbutton(
    window, bg="#383838", fg="white", activebackground="#383838",
    selectcolor="#383838", text="Only Audio", activeforeground="white",
    font=("Arial", 15), variable=onlyAudio, onvalue=True, offvalue=False
)

dlButton = tk.Button(
    window, text="Download", fg="white", bg="#2C2C2C", border=0,
    activebackground="#1E1E1E", font=("Arial", 15), activeforeground="white",
    command=lambda: download(onlyAudio=onlyAudio.get(), isPlaylist=isPlaylist.get(), link=linkEntry.get())
)

def bytes_to_megabytes(bytes_size):
    return bytes_size / (1024 ** 2)

def progress_func(stream, chunk, bytes_remaining):
    current = stream.filesize - bytes_remaining
    done = int(50 * current / stream.filesize)

    # Texte de progression complet
    progress_text = f"[{'=' * done}{' ' * (50 - done)}] {bytes_to_megabytes(current):.2f} MB / {bytes_to_megabytes(stream.filesize):.2f} MB"

    # Réduire la taille de la police si le texte dépasse
    max_width = window.winfo_width() - 20  # Largeur maximale disponible
    font_size = 15
    while len(progress_text) * font_size > max_width and font_size > 8:  # Réduire la taille de la police
        font_size -= 1

    progressBarLabelVideo.config(font=("Arial", font_size), text=progress_text)
    window.update()


def complete_func(stream, file_path):
    def update_label():
        progressBarLabelVideo["text"] = f"Finished downloading"

    window.after(0, update_label)

def dlVideo(link, onlyAudio=False, folder="downloads", isPlaylist=False, event=None):
    def download_task():
        try:
            yt = YouTube(
                link,
                on_complete_callback=complete_func,
                on_progress_callback=progress_func
            )

            if onlyAudio:
                yt.streams.get_audio_only().download(folder)
            else:
                yt.streams.get_highest_resolution().download(folder)

        except Exception as e:
            progressBarLabelVideo["text"] = f"Error: {str(e)}"

    # Lancer le téléchargement dans un nouveau thread
    threading.Thread(target=download_task).start()

def dlPlaylist(link, onlyAudio=False, folder="downloads"):
    pl = Playlist(link)
    i = 0

    def download_task(video_url):
        nonlocal i  # Declare that `i` belongs to the enclosing scope
        try:
            yt = YouTube(
                video_url,
                on_progress_callback=progress_func
            )

            if onlyAudio:
                yt.streams.get_audio_only().download(folder)
            else:
                yt.streams.get_highest_resolution().download(folder)

        except Exception as e:
            progressBarLabelVideo["text"] = f"Error: {str(e)}"
            
        i += 1

        pourcentage = (i / len(pl.video_urls)) * 100
        done = int(50 * pourcentage / 100)

        progressText =f"[{'=' * done}{' ' * (50 - done)}] {i} of {len(pl.video_urls)}"
        max_width = window.winfo_width() - 20
        font_size = 15
        while len(progressText) * font_size > max_width and font_size > 8:
            font_size -= 1

        progressBarLabelPlaylist.config(font=("Arial", font_size), text=progressText)

        progressBarLabelPlaylist["text"] = progressText
        if i == len(pl.video_urls):
            progressBarLabelPlaylist["text"] = "Done"

    for video_url in pl.video_urls:
        threading.Thread(target=download_task, args=(video_url,)).start()

def download(onlyAudio, isPlaylist, folder="downloads", link=""):
    if isPlaylist:
        dlPlaylist(link, onlyAudio=onlyAudio, folder=folder)
    else:
        dlVideo(link, onlyAudio=onlyAudio, folder=folder)


# Placement des éléments
titleLabel.place(relx=0.5, rely=0.1, anchor="center")
linkLabel.place(relx=0.1, rely=0.3, anchor="w")
linkEntry.place(relx=0.1, rely=0.4, anchor="w", relwidth=0.8)
playlistCheckButton.place(relx=0.1, rely=0.5, anchor="w")
onlyAudioCheckButton.place(relx=0.3, rely=0.5, anchor="w")
dlButton.place(relx=0.5, rely=0.6, anchor="center", relwidth=0.8)
progressBarLabelVideo.place(relx=0.5, rely=0.7, anchor="center")
progressBarLabelPlaylist.place(relx=0.5, rely=0.8, anchor="center")

# Démarrer la fenêtre
window.mainloop()