from pytube import YouTube
link=input("Enter your link.")
video=YouTube(link)
stream=video.streams.get_highest_resolution()
stream.download()