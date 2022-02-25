import pytube
from os import mkdir

def video(link):
    yt = pytube.YouTube(link)
    print("Título: ", yt.title)
    print("Número de views: ", yt.views)
    print("Tamanho do vídeo: ", yt.length, "segundos")
    print("Avaliação do vídeo: ", yt.rating)
    print(f"Criador: {yt.author}")
    ys = yt.streams.get_highest_resolution()
    print("Baixando...")
    ys.download(f"./{yt.title}.mp4")
    print("Baixado")


def playlist(link):
    yt = pytube.Playlist(link)
    print(f"Título: {yt.title}")
    print(f"Vídeos: {yt.length}")
    print(f"Criador: {yt.owner}")
    print(f"Descrição: {yt.description}")
    mkdir(yt.title)
    for indice, video in enumerate(yt.videos):
        print(f'Baixando vídeo {indice + 1}/{yt.length}')
        video.streams.get_highest_resolution().download()
    print("Todos os vídeos foram baixados!")

