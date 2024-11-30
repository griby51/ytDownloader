import sys
from pytubefix import YouTube, Playlist
from pytubefix.exceptions import *
from tqdm import tqdm

#i found that on internet, i don't know how that work LOL
def progress_func(stream, chunk, bytes_remaining):
    current = stream.filesize - bytes_remaining
    done = int(50 * current / stream.filesize)

    sys.stdout.write(
        "\r[{}{}] {} MB / {} MB".format('=' * done, ' ' * (50 - done), "{:.2f}".format(bytes_to_megabytes(current)),
                                        "{:.2f}".format(bytes_to_megabytes(stream.filesize))))
    sys.stdout.flush()

def bytes_to_megabytes(bytes_size):
    megabytes_size = bytes_size / (1024 ** 2)
    return megabytes_size


def dlVideo(video_url, onlyAudio = False, folder = "downloads"):
    try :
        yt = YouTube(video_url, on_progress_callback=progress_func)
        if onlyAudio:
            yt.streams.get_audio_only().download(folder)
            return
        yt.streams.get_highest_resolution().download(folder)
    except VideoUnavailable:
        print("Video unavailable or age restriction")

    except VideoPrivate:
        print("Video private")

    except VideoRegionBlocked:
        print("Video region blocked")

def dlPlaylist(playlist_url, onlyAudio = False, folder = "downloads"):
    pl = Playlist(playlist_url)
    pl_lenght = len(pl.video_urls)
    i = 1
    for video_url in tqdm(pl.video_urls, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", ascii=True, colour="green"):
        try:
            yt = YouTube(video_url, on_progress_callback=progress_func)
            if onlyAudio:
                yt.streams.get_audio_only().download(folder)
            elif onlyAudio == False:
                yt.streams.get_highest_resolution().download(folder)

        except VideoUnavailable:
            print("Video unavailable or age restriction")

        except VideoPrivate:
            print("Video private")

        except VideoRegionBlocked:
            print("Video region blocked")


        
        print(" | ", yt.title)
        i += 1
        # print ("Progression : ", (i - 1)/ pl_lenght * 100, "%", " [", "]")

# def main():
#     url = input("Enter playlist url or video url : ")
#     onlyAudio = input("Download only audio ? (y/n) : ")
#     if onlyAudio == "y" or onlyAudio == "Y":
#         onlyAudio = True
#     else:
#         onlyAudio = False
#     print("Downloading... Control C to stop")
#     if "list" in url:
#         dlPlaylist(url, onlyAudio)
#     else:
#         dlVideo(url, onlyAudio)
#     print("Done")

# main()

    