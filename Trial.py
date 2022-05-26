import cv2
import speech_recognition as sr
import pyttsx3
  
  
cap = cv2.VideoCapture(0)
  
while(True):
      
    ret, frame = cap.read()
  
    font = cv2.FONT_HERSHEY_SIMPLEX
  

    
    r = sr.Recognizer()

    try:
      with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.0000000000000000000000000002)
        audio = r.listen(source)
        print("Recognizing...")
        text = r.recognize_google(audio, language="en-US")
        print(text)
        cv2.putText(frame,text,(240, 470),font, 1,(0, 255, 255),2,cv2.LINE_4)
        cv2.imshow('video', frame)

    except sr.UnknownValueError():
      r = sr.Recognizer()
      continue
        
       
        #cv2.putText(frame,text,(240, 470),font, 1,(0, 255, 255),2,cv2.LINE_4)
  
    # Display the resulting frame
    #cv2.imshow('video', frame)
  
    # creating 'q' as the quit 
    # button for the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# release the cap object
cap.release()
# close all windows
cv2.destroyAllWindows()
