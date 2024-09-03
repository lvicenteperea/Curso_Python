from pytube import YouTube
# pip install pytube

def descargar_video(url, path):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path=path)
        print(f'Video descargado: {yt.title}')
    except Exception as e:
        print(f'Error: {e}')

# URL del video de YouTube
url = 'https://www.youtube.com/watch?v=XXXXXXXXXXX'
# Ruta donde se descargará el video
path = './'

descargar_video(url, path)

'''
Al mas chapucero:
from pytube import YouTube

url = 'https://www.youtube.com/watch?v=sVPYIRF9RCQ'

yt = YouTube(url)

video = yt.streams.order_by('resolution').desc()[0]

output = './Test'

video.download(output)

'''