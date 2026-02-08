import cv2
#좌우 대칭
img=cv2.imread('openCV\cat.jpg')
flip_horizontal=cv2.flip(img,1) #1:좌우대칭,0:상하대칭,-1:상하좌우대칭

cv2.imshow('img',img)
cv2.imshow('flip_horizontal',flip_horizontal)


#상하 대칭
flip_vertical=cv2.flip(img,0)
cv2.imshow('flip_vertical',flip_vertical)

#상하좌우대칭
flip_horizontal_vertical=cv2.flip(img,-1)
cv2.imshow('flip_horizontal_vertical',flip_horizontal_vertical)

cv2.waitKey(0)
cv2.destroyAllWindows()