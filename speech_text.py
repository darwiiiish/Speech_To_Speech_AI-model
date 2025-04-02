import speech_recognition as sr
import time

def listen_with_timeout(timeout=20):

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print(f"You have {timeout} seconds to speak. Say 'thank you' to stop early.")
        recognizer.adjust_for_ambient_noise(source)

        start_time = time.time()  
        audio_data = []

        while time.time() - start_time < timeout:

            try:
                print("Listening...")

                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5) 
                text = recognizer.recognize_google(audio)

                print("You said:", text)

                audio_data.append(text)  

                if "thanks" in text: 
                    print("Detected 'thanks', stopping early.")
                    break
                
            except sr.WaitTimeoutError:
                print("No speech detected, please speak.")
            except sr.UnknownValueError:
                print("Could not understand, please try again.")
            except sr.RequestError:
                print("API request error, check your connection.")

        return "answer breifely on any question and dont write any code : " + " ".join(audio_data)


