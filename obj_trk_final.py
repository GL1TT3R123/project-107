import cv2
import time
import math 

p1=530
p2=300

xs=[]
ys=[]

video=cv2.VideoCapture("footvolleyball.mp4")

tracker=cv2.TrackerCSRT_create()

returned,image = video.read()

#select bounding box on the image
Bbox= cv2.selectROI("tracking",image,False)
tracker.init(image,Bbox)

def DrawBox(image,Bbox):
    x,y,w,h= int(Bbox[0]),int(Bbox[1]),int(Bbox[2]),int(Bbox[3])
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),3,1)

def GoalTrack(image,Bbox):
    x,y,w,h= int(Bbox[0]),int(Bbox[1]),int(Bbox[2]),int(Bbox[3])
    
    #get the center piont of the bounding box
    c1= x+int(w/2)
    c2=y+int(h/2)

    #draw the small circle using center point
    cv2.circle(image,(c1,c2),2,(0,0,255),3)
    cv2.circle(image,(p1,p2),2,(0,0,255),3)

    distance=math.sqrt((c1-p1)**2+(c2-p2)**2)
    if (distance<=20):
        cv2.putText(image,"Goal",(300,90),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)
    xs.append(c1) 
    ys.append(c2)  
    for i in range(len(xs)-1):
        cv2.circle(image,(xs[i],ys[i]),2,(0,255,0),5)
while True:
    check,image =video.read()
    success,Bbox= tracker.update(image)

    if success :
        DrawBox(image,Bbox)
    GoalTrack(image,Bbox)
    cv2.imshow("window",image)
    key=cv2.waitKey(25)
    if key==32:
        break
video.release()
cv2.destroyAllWindows()    





