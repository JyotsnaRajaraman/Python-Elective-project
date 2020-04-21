import numpy as np 
import cv2
import time

#take a realtime image
camera = cv2.VideoCapture(0)
for i in range(10):
    return_value, image = camera.read()
    cv2.imwrite("rtimg.jpg", image)
del(camera)

#make a copy of the original image
img = cv2.imread('rtimg.jpg', cv2.IMREAD_UNCHANGED)
cv2.imwrite('rtimg2.jpg', img)

while True:
	#read image
	im = cv2.imread('rtimg2.jpg',cv2.IMREAD_UNCHANGED)

	#select ROI
	r = cv2.selectROI(im)

	#crop
	imCrop = im[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]

	#zoom
	scale_percent = 450
	#scale_percent = int(input ("enter : "))
	width = int(imCrop.shape[1] *scale_percent / 100)
	height = int(imCrop.shape[0] *scale_percent / 100)
	dim =(width,height)
	imZoom = cv2.resize(imCrop,dim,interpolation = cv2.INTER_AREA)

	#save cropped
	cv2.imwrite('rtimg2.jpg', imZoom)


	#ask for continuation
	try_again = int(input("Press 1 to try again, 0 to exit. "))
	if try_again == 0:
		cv2.imwrite('finalzoomedimg.jpg', imZoom)
		break 

#show zoomed image
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_PLAIN
        strBGR = str(blue) + ', '+ str(green)+ ', '+ str(red)
        cv2.putText(img, strBGR, (x, y), font, 1, (0, 0, 0), 2)
        cv2.imshow('image', img)
cap = cv2.imread('finalzoomedimg.jpg')

#print BGRo values of intersection of ROI
cap = cv2.resize(cap, (340,480))
color = cap[240,175]
print ('the BGR of the centre pixel is: ', color)
print ("you can touch anywhere on the picture to display the RGB as well\n press 0 to exit")
img = cv2.imread('finalzoomedimg.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

#press 0 to close all windows

cv2.waitKey(0)
cv2.destroyAllWindows()


