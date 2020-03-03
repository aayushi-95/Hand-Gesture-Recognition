import cv2
import numpy as np
import math
import time
from pymouse import PyMouse
m = PyMouse()
cap = cv2.VideoCapture(0)
cap.set(3,800)
cap.set(4,600)
while(cap.isOpened()):
    ret, x = cap.read()
    img = cv2.flip(x,90)
    ycbcr = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    blur = cv2.GaussianBlur(ycbcr,(35,35),0)
    ycbcrMIN = np.array([0, 133, 77],np.uint8)
    ycbcrMAX = np.array([255, 173, 127],np.uint8)
    ycbcrFilterImg = cv2.inRange(blur,ycbcrMIN,ycbcrMAX)
    _, contours, hierarchy = cv2.findContours(ycbcrFilterImg.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    max_area = -1
    for i in range(len(contours)):
        cnt=contours[i]
        area = cv2.contourArea(cnt)
        if(area>max_area):
            max_area=area
            ci=i
    cnt=contours[ci]
    x,y,w,h = cv2.boundingRect(cnt)
    hull = cv2.convexHull(cnt)
    drawing = np.zeros(img.shape,np.uint8)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
    cv2.drawContours(drawing,[hull],0,(0,0,255),0)
    hull = cv2.convexHull(cnt,returnPoints = False)
    defects = cv2.convexityDefects(cnt,hull)
    count_defects = 0
    cv2.drawContours(ycbcrFilterImg, contours, -1, (255,0,0), 3)
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
        if angle <= 90:
            count_defects += 1
            cv2.circle(img,far,1,[0,0,255],-1)
        dist = cv2.pointPolygonTest(cnt,far,True)
        cv2.line(img,start,end,[0,255,0],2)
        cv2.circle(img,far,5,[0,0,255],-1)
    m.move(x,y)
    if count_defects == 1:
        cv2.putText(img,"ONE", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        #m.press(cx,cy,1)
    elif count_defects == 2:
        cv2.putText(img, "TWO", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif count_defects == 3:
        cv2.putText(img,"THREE", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif count_defects == 4:
        cv2.putText(img,"FOUR", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif count_defects == 5:
        cv2.putText(img,"FIVE", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    else:
        cv2.putText(img,"OVER/UNDER FLOW", (50,50),cv2.FONT_HERSHEY_SIMPLEX, 1, 1)
    #cv2.imshow('drawing', drawing)
    #cv2.imshow('end', crop_img)
    cv2.imshow('Gesture', img)
    cv2.imshow('threshold',ycbcrFilterImg)
    k = cv2.waitKey(10)
    if k == 27:
        break
