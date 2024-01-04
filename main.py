import cv2
import numpy as np
import os 

# read image 
img = cv2.imread(r"me.jpg",-1)
#cv2.imshow("Bharat",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#resize image 
re_img = cv2.resize(img,(500,500))
#cv2.imshow("Bharat",re_img)
#cv2.waitKey(0)

#pixels in image 
#print(img)

#Multiple images in one Frame 
#img_arr = np.array([[1,2,1,2],[1,2,1,2]])
#h = np.hstack((re_img,re_img))
#v = np.vstack((h,h,h))
#cv2.imshow("Bharat",v)
#cv2.waitKey(0)

#image-Read(flags)
#cv2.IMREAD_COLOR ==> load a color image(Default flag), Integer-value : 1
#cv2.IMREAD_GRAYSCALE ==> load img in grayscale mode , Integer-value : 0
#cv2.IMREAD_UNCHANGED ==> load img with alpha-parameter , Integer-value : -1
#print(img.shape)
#cv2.imshow("Bharat",re_img)
#cv2.waitKey(0)

#Text on img
text = "Bharat"
org = (150,50)
font_face = cv2.FONT_HERSHEY_DUPLEX
font_scale = 2
color = (255,0,255)
thick = 2
line_type =cv2.LINE_8

txt = cv2.putText(re_img,text,org,font_face,font_scale,color,thick,line_type,False)
cv2.imshow("Bharat",re_img)
cv2.waitKey(0)
