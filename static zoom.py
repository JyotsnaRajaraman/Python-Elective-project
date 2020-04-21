import time
import cv2

#take a realtime image
camera = cv2.VideoCapture(0)
for i in range(10):
    return_value, image = camera.read()
    cv2.imwrite("original.png", image)
del(camera)
img = cv2.imread('original.png', cv2.IMREAD_UNCHANGED)
d = img.shape
print(d[0:2])
#select ROI
r = cv2.selectROI(img)

	#crop
imgCrop = img[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]

scale_percent = 300 # percent of original size
width = int(imgCrop.shape[1] * scale_percent / 100)
height = int(imgCrop.shape[0] * scale_percent / 100)
dim = (width, height)
print(dim)

# resize image
resized = cv2.resize(imgCrop, dim, interpolation = cv2.INTER_AREA)


cv2.imshow("original image", img)
cv2.imshow("Resized image", resized)
#press 0 to close all windows

cv2.waitKey(0)
cv2.destroyAllWindows()



