from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stoper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_user=input("input for stop")
        if input_user == stoper:
            mixer.music.stop()
            break
def blog(msg):
    with open("blog.txt","a") as f:
        f.write(f"{msg} at {datetime.now()}")

if __name__=='__main__':
    init_water = time()
    init_eye=time()
    init_exe=time()
    watersec=5
    eyesec=10
    exesec=7

    while True:
        if time()-init_water >watersec:
            print("water....Enter w to stop.")
            musiconloop("music.mp3","w")
            init_water=time()
            blog("water\n")
        if time()-init_eye >eyesec:
            print("eye....Enter E to stop.")
            musiconloop("music.mp3","E")
            init_eye=time()
            blog("eye\n")
        if time()-init_exe >exesec:
            print("exercise....Enter x to stop.")
            musiconloop("music.mp3","x")
            init_exe=time()
            blog("exercise\n")
            