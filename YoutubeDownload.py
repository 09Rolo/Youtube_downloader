from pytube import YouTube
import os

import ffmpeg
import time


print("-----------------------------------------------------------------------------------")
print(" Videó(v)(valószínűleg 720p max) vagy Zene?(z)   |   vagy magas minőségű videó(mm)")
print("-----------------------------------------------------------------------------------")
vidvagymusic = input("\n>> ")




if vidvagymusic == "v":
    link = input("\nLink: ")
    video = YouTube(link)


    stream_video = video.streams.get_highest_resolution()

    print("\n----------")
    print("Videó: " + video.title)
    print("Legnagyobb képminőség: " + stream_video.resolution)
    print("----------")

    print("\nLetöltés...")
    stream_video.download()
    

    print("\n------")
    print(" Kész!")
    print("------")





elif vidvagymusic == "z":
    link = input("\nLink: ")
    video = YouTube(link)


    abrlista = []
    for v in video.streams.filter():
        if not v.abr == None:

            currentabr = int(v.abr[:-4])

            if not currentabr in abrlista:
                abrlista.append(currentabr)

    
    list = sorted(abrlista, reverse=True)
    highestabr = str(list[0]) + "kbps"

    stream_audio = video.streams.filter(abr=highestabr).first()


    print("\n----------")
    print("Zene: " + video.title)
    print("Legnagyobb kbps: " + highestabr)
    print("----------")

    print("\nLetöltés....")



    stream_audio.download(filename="audio.file")
    
    cmd = "ffmpeg -i {} -vn {}".format("audio.file", "audio.mp3")
    os.system(cmd)


    try:
        os.rename("audio.mp3", video.title + ".mp3")
    except:
        os.rename("audio.mp3", "NEVEZD_ÁT.mp3")


    os.remove("audio.file")
    

    print("\n------")
    print(" Kész!")
    print("------")





elif vidvagymusic == "mm":
    link = input("\nLink: ")
    video = YouTube(link)
    print("\nLetöltés....")


    print("\n----------")
    print("Videó: " + video.title)




    resolutionlista = []
    for v in video.streams:
        if not v.resolution == None:

            currentres = int(v.resolution[:-1])

            if not currentres in resolutionlista:
                resolutionlista.append(currentres)

    

    list = sorted(resolutionlista, reverse=True)
    highestres = str(list[0]) + "p"
    print("Legnagyobb képminőség: " + highestres)

    stream_video = video.streams.filter(res=highestres, adaptive=True).first()
    stream_video.download(filename="video.mp4")






    abrlista = []
    for v in video.streams.filter(only_audio=True):
        if not v.abr == None:

            currentabr = int(v.abr[:-4])

            if not currentabr in abrlista:
                abrlista.append(currentabr)

    
    list = sorted(abrlista, reverse=True)
    highestabr = str(list[0]) + "kbps"
    print("Legnagyobb hangminőség: " + highestabr)


    stream_audio = video.streams.filter(abr=highestabr).first()

    out_file = stream_audio.download(filename='hang.mp3')
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)


    print("----------")




    print("\nÖsszeolvasztás...")


    video_file = ffmpeg.input("video.mp4")
    audio_file = ffmpeg.input("hang.mp3")


    try:
        ffmpeg.output(audio_file, video_file, video.title + "_hanggal.mp4").run()
    except:
        ffmpeg.output(audio_file, video_file, "NEVEZD_ÁT" + "_hanggal.mp4").run()



    time.sleep(5)
    os.remove("video.mp4")
    os.remove("hang.mp3")



    print("\n------")
    print(" Kész!")
    print("------")

