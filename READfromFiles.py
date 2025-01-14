from gtts import gTTS  # python libarary for text to audio
import os
text=open('sample.txt','r').read()
output=gTTS(text=text,lang='en',slow=False)
output.save('fileoutput.mp3')
os.system("start fileoutput.mp3")

# for other language codes just search google speech language codes

