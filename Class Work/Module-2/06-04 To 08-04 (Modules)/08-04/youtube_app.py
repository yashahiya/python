from pytubefix import YouTube

url="https://www.youtube.com/watch?v=pP1PPDGasEM&t=1225s"

YouTube(url).streams.first().download()