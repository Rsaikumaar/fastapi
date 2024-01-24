from gtts import gTTS
import os
# Text you want to convert to speech
text = '''
'''
# Create a gTTS object
tts = gTTS(text)
# Save the audio file
tts.save("output.mp3")
# Play the audio file (platform dependent, uses 'afplay' on macOS)
os.system("start output.mp3")  # for Windows
