import cv2 as cv
from moviepy.editor import *
import speech_recognition as sr
import pyttsx3
import pyaudio
import time

cap = cv.VideoCapture(0)

if (cap.isOpened() == False):
  print("Unable to read camera feed")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter('outpy.mp4',cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while(True):
    ret, frame = cap.read()
    out.write(frame)
    print(time.clock())
    if (10 < time.clock() <= 12):
      cv.putText(frame, "Assalam O Alaikum. ", (240, 470), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3) 
      cv.imshow('Original', frame)
      print(0)

    elif (13 < time.clock() <= 15):
      cv.putText(frame, "I am Ameema Arif and I am Memoona Arif.", (240, 470), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3) 
      cv.imshow('Original', frame)
      print(1)

    elif (16 < time.clock() <= 20):
      cv.putText(frame, "We are trying to make a superficial app.", (240, 470), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3) 
      cv.imshow('Original', frame)
      print(2)

    elif (21 < time.clock() <= 25):
      cv.putText(frame, "This app is called live subtitles.", (240, 470), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3) 
      cv.imshow('Original', frame)
      print(3)

    elif time.clock() == 28:
      break
    elif cv.waitKey(1) & 0xFF == ord('q'):
            break
    print("here")
    #cv.imshow('Original', frame)
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv.destroyAllWindows()
