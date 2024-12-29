import cv2 as cv
import numpy as np

imgpath = "C:/Users/91628/Downloads/adr.jpeg"
img = cv.imread(imgpath)

if img is None:
    print("Image not found or unable to load.")
    exit()

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lpurple = (125, 40, 40)
upurple = (155, 255, 255)
purplemask = cv.inRange(hsv, lpurple, upurple)

lred1 = (0, 40, 40)
ured1 = (10, 255, 255)
lred2 = (160, 40, 40)
ured2 = (180, 255, 255)
redmask = cv.inRange(hsv, lred1, ured1) | cv.inRange(hsv, lred2, ured2)

combined_mask = purplemask | redmask

cv.imshow("Purple Mask", purplemask)
cv.imshow("Red Mask", redmask)
cv.imshow("Combined Mask", combined_mask)

contours, _ = cv.findContours(combined_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

min_area = 50  
max_area = 8000


for cnt in contours:
    area = cv.contourArea(cnt)
    if area < min_area or area > max_area:
        continue

    x, y, w, h = cv.boundingRect(cnt)
    aspect_ratio = w / h

  
    if 0.3 < aspect_ratio < 3.0:  
        if np.any(purplemask[y:y+h, x:x+w]):
            color = (255, 0, 255) 
        elif np.any(redmask[y:y+h, x:x+w]):
            color = (0, 0, 255) 
        else:
            continue
        cv.rectangle(img, (x, y), (x + w, y + h), color, 2)


cv.imshow("Detected Fruits", img)
cv.waitKey(0)
cv.destroyAllWindows()



 









