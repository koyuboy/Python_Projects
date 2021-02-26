import cv2
import numpy as np

#Converting the gif to jpg
gif = cv2.VideoCapture('chromium alloy.gif')
ret, frame = gif.read()
cv2.imwrite('chromium alloy.jpg', frame)
 
#reading the image
image = cv2.imread("chromium alloy.jpg", 0)
#shows the results
cv2.imshow("canny",	image)






#read the image
image = cv2.imread("800.jpg")
kernel = np.array([[-1,-1,-1], [-1, 9,-1], [-1,-1,-1]])

# uses sharpening kernel
sharpened = cv2.filter2D(image, -1, kernel) 
#shows the result
cv2.imshow('SharpenedImage', sharpened)





#importing the image
pipes	= cv2.imread('pipes.jpg')
gray_img	=	cv2.cvtColor(pipes,	cv2.COLOR_BGR2GRAY)
img	= cv2.medianBlur(gray_img,	5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)


#parameters
circles	= cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,2,52,param1=160,param2=50,minRadius=14,maxRadius=97)
circles	= np.uint16(np.around(circles))

for	i in circles[0,:]:
    
				#	draw	the	outer	circle
				cv2.circle(pipes,(i[0],i[1]),i[2],(0,255,0),2)

#showing the results
cv2.imshow("Circles",	pipes)
cv2.waitKey()
cv2.destroyAllWindows()