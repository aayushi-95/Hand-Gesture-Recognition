
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
# Capture frame-by-frame
	ret, frame = cap.read()
	# Our operations on the frame come here
	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	frameResize = cv2.resize(frame, (400, 300))
	hsv = cv2.cvtColor(frameResize,cv2.COLOR_BGR2HSV)
	hsvMIN = np.array((0,30,60))
	hsvMAX = np.array((20,150,179))
	hsvFilterImg = cv2.inRange(hsv,hsvMIN,hsvMAX)
	ycbcr = cv2.cvtColor(frameResize,cv2.COLOR_BGR2YCR_CB)
	ycbcrMIN = np.array((0, 133, 77))
	ycbcrMAX = np.array((255, 173, 127))
	ycbcrFilterImg = cv2.inRange(ycbcr,ycbcrMIN,ycbcrMAX)
	# _ ,thresh1 = cv2.threshold(ycbcr, 127, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	# Display the resulting frame 
	img_and = cv2.bitwise_and(hsvFilterImg,ycbcrFilterImg)
	cv2.imshow('OrigImg',frameResize)
	cv2.imshow('HSV',hsv)
	cv2.imshow('YCbCr',ycbcr)
	cv2.imshow('AND',img_and)
	# cv2.imshow('Threshold',thresh1)
	# cv2.imshow('True',frame)
	cv2.imshow('HSVFilter',hsvFilterImg)
	cv2.imshow('YCBCRFilter',ycbcrFilterImg)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
