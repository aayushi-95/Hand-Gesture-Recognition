# Hand-Gesture-Recognition
Human Computer Interaction implemented using Raspberry Pi

### Libraries : Numpy, OpenCV, Raspbian

**Aim** Build a gesture vocabulary (static and dynamic) which when matched with the captured image triggers a specific function: a particular msuical note- a guitar cord or drum string.

### Workflow 
- [x] Video Acquistion via Rasperry Pi Camera Module
- [x] Background Subtraction - Gaussian Blur and Thresholding
- [x] Finding Contour and draw Convex Hull
- [x] Find onvexity Defects to count the number of images

![](https://github.com/aayushi-95/Hand-Gesture-Recognition/blob/master/images/five.png)

_Challenges faced_
1) Hand Tracking for dynamic gesture
    - Centroid tracking (take palm as center) - KLT Tracking
2) Remove obstacle to recogonize only the skin color
    - Convert Image to Grayscale - Apply HSV and YCbCr plane for extracting skin color - Perform logical AND of both planes - Extract largest connected area


![](https://github.com/aayushi-95/Hand-Gesture-Recognition/blob/master/images/remove%20pen.png)
