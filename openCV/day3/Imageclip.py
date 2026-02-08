#이미지 자르기
import cv2
#영역 잘라서 새로운 윈도우(창)에 표시
img=cv2.imread('openCV\cat.jpg')
# print(img.shape)

crop=img[100:200,200:400] #세로100~200,가로300~400

cv2.imshow('img',img)
cv2.imshow('crop',crop)
cv2.waitKey(0)
cv2.destroyAllWindows()

#영역을 잘라서 기존 윈도우에 표시
img2=cv2.imread('openCV\cat.jpg')

img2[200:300,200:400]=crop

cv2.imshow('img',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()