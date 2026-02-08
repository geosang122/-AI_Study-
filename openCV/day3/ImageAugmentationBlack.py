#이미지 변형(흑백)
#불러온 이미지 흑백으로 변경
import cv2
'''
img=cv2.imread('openCV\cat.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

img=cv2.imread('openCV\cat.jpg')
dst=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
