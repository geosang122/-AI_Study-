import cv2
import numpy as np
#사다리꼴 이미지 펼치기

img=cv2.imread('openCV/newspaper.jpg')

width,height=640,240
src=np.array([[511,352],[1008,345],[1122,584],[455,594]],dtype=np.float32) #Input 4개 지점
dst=np.array([[0,0],[width,0],[width,height],[0,height]],dtype=np.float32) #Output 4개 지점

matrix=cv2.getPerspectiveTransform(src,dst) #변환 행렬 계산
result=cv2.warpPerspective(img,matrix,(width,height)) #원근 변환 적용

cv2.imshow('img',img)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()

#회전된 이미지 펼치기
img=cv2.imread('openCV/poker.jpg')

width,height=530,710
src=np.array([[702,143],[1133,414],[726,1007],[276,700]],dtype=np.float32) #Input 4개 지점
dst=np.array([[0,0],[width,0],[width,height],[0,height]],dtype=np.float32) #Output 4개 지점

matrix=cv2.getPerspectiveTransform(src,dst) #변환 행렬 계산
result=cv2.warpPerspective(img,matrix,(width,height)) #원근 변환 적용

cv2.imshow('img',img)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()