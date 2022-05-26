import cv2 as cv
from moviepy.editor import *
import speech_recognition as sr
import pyttsx3
import pyaudio
import time

cap = cv.VideoCapture(0)
r = sr.Recognizer()
s = 0
e = 1

if (cap.isOpened() == False):
  print("Unable to read camera feed")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter('outpy.mp4',cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while(True):
    ret, frame = cap.read()
    out.write(frame)
    time.sleep(1001)
    try:
      with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        text = r.recognize_google(audio, language="en-US")

    except sr.UnknownValueError():
      r = sr.Recognizer()
      continue
        
    cv.putText(frame, text, (240, 470), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3) 
    cv.imshow('Original', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
            break


# After the loop release the cap object
cap.release()
# Destroy all the windows
cv.destroyAllWindows()
