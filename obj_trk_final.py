import cv2
import time
import math
video=cv2.VideoCapture("footvolleyball.mp4")
#load tracker
tracker=cv2.TrackerCSRT_create()
check,img=video.read()
bbox=cv2.selectROI("Tracking",img,False)
tracker.init(img,bbox)

def drawBox(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)



while True:
  check,img=video.read()
  success,bbox=tracker.update(img)
  if success:
        drawBox(img,bbox)
  else:
    cv2.putText(img,"lost",(75,90),cv2.FONT_HERSHEY_COMPLEX,0.7,(20,30,200),2)
    #putTExt(imgae,word,position,font_style,thickness,color,size)
    cv2.imshow("output",img)
    key=cv2.waitKey(25)
    if key==32:
        print("stopped")
        break
video.release()
cv2.destroyAllWindows()