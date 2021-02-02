# imports
import cv2  
import numpy as np  

# initializing the videocapture and reading the image
video = cv2.VideoCapture(0) 
image = cv2.imread("bg.jfif") 
  
# while loop
while True: 
    # reading the video
    ret, frame = video.read() 

    # resizing the image
    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 
  
    # the color ranges
    u_black = np.array([104, 153, 70]) 
    l_black = np.array([30, 30, 0]) 
    
    # the mask using inrange of cv2
    mask = cv2.inRange(frame, l_black, u_black) 
    
    # the result
    res = cv2.bitwise_and(frame, frame, mask = mask) 
    
    # using the np.where fumction
    f = frame - res 
    f = np.where(f == 0, image, f) 
    
    # displaying the image in a window using imshow
    cv2.imshow("video", frame) 
    cv2.imshow("mask", f) 
    
    # breaking the while loop if escape or q is pressed
    k = cv2.waitKey(1)
    if k == 27 or k == ord('q'):
        break 

# destroying all the windows and closing the screens
video.release() 
cv2.destroyAllWindows() 
