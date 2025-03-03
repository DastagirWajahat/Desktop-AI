from tkinter import * #pip install tkinter
from PIL import Image,ImageTk,ImageSequence #pip install Pillow
import time
import pygame  #pip install pygame
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("1000x500")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("ai.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("Startup2.mp3")
    mixer.music.play()

    start_time=time.time()
    
    while time.time()-start_time < 3:
        for frame in ImageSequence.Iterator(img):
            frame = frame.resize((1000, 500))
            frame = ImageTk.PhotoImage(frame)
            
            # Update the label with the current frame
            lbl.config(image=frame)
            
            # Refresh the window
            root.update()
            
            # Pause for a short duration between frames
            time.sleep(0.05)    

            if time.time()-start_time > 3:
                break

    
    # for img in ImageSequence.Iterator(img):
    #     img = img.resize((1000,500))
    #     img = ImageTk.PhotoImage(img)
    #     lbl.config(image=img)
    #     root.update()
    #     time.sleep(0.05)
    # root.destroy()
    mixer.music.stop()
    root.destroy()

play_gif()
root.mainloop()
