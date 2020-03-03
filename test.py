import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        ycbcr=cv2.cvtColor(frame,cv2.COLOR_BGR2YCR_CB)
        # Display the resulting frame
        cv2.imshow('HSV',hsv)
        cv2.imshow('YCbCr',ycbcr)
        cv2.imshow('True',frame)
        thresh1 = cv2.threshold(ycbcr, 127, 255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
