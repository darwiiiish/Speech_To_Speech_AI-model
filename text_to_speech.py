from gtts import gTTS
import io
import pygame

def text_to_speech(text):
    tts = gTTS(text=text, lang="en", tld="com.au", slow=False)
    audio_stream = io.BytesIO()
    tts.write_to_fp(audio_stream)
    audio_stream.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(audio_stream, "mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        continue
