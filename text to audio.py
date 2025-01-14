from gtts import gTTS  # python libarary for text to audio
import os
text="hello sumedh how are u ?"
output=gTTS(text=text,lang='en',slow=False)
output.save('output.mp3')
os.system("start output.mp3")

# for other language codes just search google speech language codes