import speech_recognition as sr
import pyttsx3
  
while(True):
    
    r = sr.Recognizer()

    try:
      with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.02)
        audio = r.listen(source)
        print("Recognizing...")
        text = r.recognize_google(audio, language="en-US")
        print(text)

    except sr.UnknownValueError():
      r = sr.Recognizer()
      continue
        
       

