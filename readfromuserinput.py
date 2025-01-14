
from gtts import gTTS  # python libarary for text to audio
import os
from tkinter import *
root=Tk()
canvas=Canvas(root,width=400,height=400)  # canvas is used to change height and width of the tkinter window
canvas.pack()
def texttospeech():
 text=entry.get()  #get what user has entered in entry box
 language='en'
 output=gTTS(text=text,lang=language,slow=False)
 output.save('output.mp3')
 os.system("start output.mp3")
entry=Entry(root)
canvas.create_window(200,180,window=entry)     # in bracket it the position of pixel of where to add the window,200 is the y co-ordinate and 180 is the x coordinate are the postion
button=Button(text="Start",command=texttospeech)
canvas.create_window(200,230,window=button)
root.mainloop()





