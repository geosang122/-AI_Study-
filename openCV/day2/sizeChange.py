import cv2
#고정 크기로 설정
img=cv2.imread("openCV/cat.jpg")
dst=cv2.resize(img,(400,500))

cv2.imshow('img',img)
cv2.imshow('resize',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
#비율로 설정

img=cv2.imread("openCV/cat.jpg")
dst=cv2.resize(img,None,fx=0.5,fy=0.5)

cv2.imshow('img',img)
cv2.imshow('resize',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
보간법(interpolation)
cv2.INTER_AREA 크기 줄일 때
cv2.INTER_CUBIC 크기 늘릴 때(속도 느림, 품질 좋음)
cv2.INTER_LINEAR크기 늘릴 때(기본)
'''
img=cv2.imread("openCV/cat.jpg")
dst1=cv2.resize(img,None,fx=0.5,fy=0.5)
dst2=cv2.resize(img,None,fx=0.5,fy=0.5, interpolation=cv2.INTER_AREA)
dst3=cv2.resize(img,None,fx=2,fy=2, interpolation=cv2.INTER_CUBIC)
dst4=cv2.resize(img,None,fx=2,fy=2, interpolation=cv2.INTER_LINEAR)

cv2.imshow('img',img)
cv2.imshow('resize1',dst1)
cv2.imshow('resize2',dst2)
cv2.imshow('resize3',dst3)
cv2.imshow('resize4',dst4)

cv2.waitKey(0)
cv2.destroyAllWindows()
