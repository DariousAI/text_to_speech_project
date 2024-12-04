# Import required modules
from gtts import gTTS
from playsound import playsound
import os

# Step 1: Define the text you want to convert to speech
text = "Hello! This is a simple text to speech application."

# Step 2: Create an 'audio' directory if it doesn't exist
audio_directory = "audio"
if not os.path.exists(audio_directory):
    os.makedirs(audio_directory)

# Step 3: Create the TTS object
tts = gTTS(text=text, lang='en')

# Step 4: Save the audio file in the 'audio' directory
audio_path = os.path.join(audio_directory, "output.mp3")
tts.save(audio_path)

# Step 5: Play the audio file
playsound(audio_path)
