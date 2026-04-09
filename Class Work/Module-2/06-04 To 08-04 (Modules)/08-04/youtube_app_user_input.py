from pytubefix import YouTube

url=input("Enter Youtube Link For Download Video : ")

YouTube(url).streams.first().download()