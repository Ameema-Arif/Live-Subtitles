# import the opencv library
import cv2
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
  
  
# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white')
    subs = "E:\FYP\Test.srt"

    subtitles = SubtitlesClip(subs, generator)
    
    i=0
    while(vid.isOpened()):
        ret, frame = vid.read()
        if ret == False:
            break
        #cv2.imwrite('input'+str(i)+'.jpg',frame)
        i+=1
        #video = VideoFileClip('input'+str(i)+'.jpg')
        frame = CompositeVideoClip([frame, subtitles.set_pos(('center','bottom'))])
        cv2.imshow('frame', frame)

        result.write_videofile("output.mp4", fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
  
    # Display the resulting frame
    #cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
