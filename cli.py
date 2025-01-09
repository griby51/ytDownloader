from pytubefix import Playlist, YouTube
import argparse
import sys
import shutil

parser = argparse.ArgumentParser(description="A simple Youtube Downloader")

parser.add_argument("url", type=str, help="Paste the link of the youtube video or playlist")

parser.add_argument("-a", "--audio", action="store_true", help="Download only the audio")

args = parser.parse_args()

#thanks u chatgpt
def showProgressBar(progress, total, prefix=""):
    terminal_width = shutil.get_terminal_size().columns
    progress_width = 25
    space_for_progress = 10

    prefix_max_len = terminal_width - progress_width - space_for_progress - 4

    if len(prefix) > prefix_max_len:
        prefix = prefix[:prefix_max_len] + "..."
    
    ratio = progress / total
    filled = int(ratio * progress_width)
    
    bar = f"{prefix}{' ' * (terminal_width - len(prefix) - progress_width - space_for_progress)}[{'#' * filled}{' ' * (progress_width - filled)}] {ratio * 100:.2f}%"
    
    sys.stdout.write(f"\r{bar}")
    sys.stdout.flush()
    if progress == total:
        print()

# def showProgressBar(progress, total, width=50, prefix=""):
#     ratio = progress / total
#     filled = int(ratio * width)
#     bar =f"[{filled * "#"}{(width - filled) * ' '}] {ratio * 100:.2f}%"
#     sys.stdout.write(f"\r{prefix}, {bar}")
#     sys.stdout.flush()

#     if progress == total:
#         sys.stdout.write("\n")

def dlVideo(url, onlyAudio = False):
    yt = YouTube(url)
    title = yt.title
    yt.register_on_progress_callback(lambda stream, chunk, bytes_remaining: showProgressBar(stream.filesize - bytes_remaining, stream.filesize, prefix=title))

    if onlyAudio:
        video = yt.streams.get_audio_only()
    else:
        video = yt.streams.get_highest_resolution()
    video.download("downloads")

dlVideo('https://www.youtube.com/watch?v=qc5bFkNj2XQ')
dlVideo('https://www.youtube.com/watch?v=_LiZWbBR96A')

# print(f"url {args.url}")
# if args.audio:
#     print("only audio")
# else:
#     dlVideo(args.url, args.audio)
