import cv2
import pandas as pd


video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FPS, 30)
num_frames = 300
text=[]

#assert len(data) == num_frames

for i in list(range(0, num_frames+1)):
    ret, frame = video.read()

    if i==0:
        data = pd.read_csv('E:/FYP/Data1.csv', usecols=["sentence"], sep=',', nrows=1)
        text.append(str(data))
        text[0]=text[0].replace('\n'," ")
        print(text[0])
        text=text[0].split()
        print(text)
        text.pop(0)
        text.pop(0)
        print(text)
        text=list(' '.join(text))
        print(text)
        print(str(i)+" in 0")

    else:
        data = pd.read_csv('E:/FYP/Data1.csv', usecols=["sentence"], sep=',', skiprows=range(1,i+1), nrows=1)
        text.append(str(data))
        print(text)
        text[0]=text[0].replace('\n'," ")
        print(text[0])
        text=text[0].split()
        print(text)
        text.pop(0)
        text.pop(0)
        print(text)
        text=' '.join(text)
        print(text)
        print(str(i)+" in 1")

        # pehle text ko kisi aur variable mein shift karo then uss variable ko return karo aur text ko clear krdo
    
    cv2.putText(frame, str(text), (240,470),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)  #, cv2.LINE_AA, True)
    cv2.imshow('Original', frame)
    text=list(text)
    print(text)
    text.clear()
    print(text)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# After the loop release the cap object
video.release()
# Destroy all the windows
cv2.destroyAllWindows()

## how to print only one row which is indexed each time
