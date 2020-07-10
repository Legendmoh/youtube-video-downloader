try:
    from  pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print("some moudle are missing {}".format(e))

url = input("Enter video link : ")
obj = YouTube(url).streams.first().download()
print(obj)


