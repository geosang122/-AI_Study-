import cv2
#시계방향 90도 회전

img=cv2.imread('openCV\cat.jpg')
rotate_90_clockwise=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('img',img)
cv2.imshow('rotate_90_clockwise',rotate_90_clockwise)

#180도 화전
rotate_180=cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow('rotate_180',rotate_180)

#시계 반대방향 90도 회전 =시계 방향 270도 회전
rotate_90_counterclockwise=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('rotate_90_counterclockwise',rotate_90_counterclockwise)
cv2.waitKey(0)
cv2.destroyAllWindows()