## 빈 스케치북 만들기
import cv2
import numpy as np
#세로 480 x 가로 640 , 3Channel(RGB)에 해당한느 스케치북 만들기
# img=np.zeros((480,640,3),dtype=np.uint8)
# img[:]=(255,255,255) #전체 흰색으로 채우기
# print(img)
# cv2.imshow('img',img)
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
일부 영역 색칠
'''
# img[100:200,200:300]=(255,255,255)
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
직선
1. cv2.LINE_4: 상하좌우 4방향으로 연결된 선
2. cv2.LINE_8: 대각선을 포함한 연결된 8방향 선 (기본값)
3. cv2.LINE_AA: 부드러운 선 (Anti-Aliasing)
'''

# img=np.zeros((480,640,3),dtype=np.uint8)
# COLOR=(0,255,255) #BGR
# THICKNESS=3

# cv2.line(img,(50,100),(400,50),COLOR,THICKNESS,cv2.LINE_8)
# #그릴 위치, 시작 점, 끝 점, 색, 두께, 선 종류
# cv2.line(img,(50,200),(400,150),COLOR,THICKNESS,cv2.LINE_4)
# cv2.line(img,(50,300),(400,250),COLOR,THICKNESS,cv2.LINE_AA)

# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
원
'''

# img=np.zeros((480,640,3),dtype=np.uint8)
# COLOR=(255,255,0) #BGR
# RADIUS=50 #반지름
# THICKNESS=10 #두께

# cv2.circle(img,(100,100),RADIUS,COLOR,THICKNESS,cv2.LINE_AA)
# #그릴 위치, 중심, 반지름, 색, 두께
# cv2.circle(img,(400,100),RADIUS,COLOR,cv2.FILLED,cv2.LINE_AA)

# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
사각형
'''
# img=np.zeros((480,640,3),dtype=np.uint8)
# COLOR=(0,255,0) #BGR
# THICKNESS=3 #두께

# cv2.rectangle(img,(100,100),(200,200),COLOR,THICKNESS)
# #그릴 위치, 왼쪽 위, 오른쪽 아래, 색, 두께
# cv2.rectangle(img,(300,100),(400,200),COLOR,-1)

# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
다각형
'''

img=np.zeros((480,640,3),dtype=np.uint8)
COLOR=(0,255,255) #BGR
THICKNESS=3 #두께
star_pts = np.array([
    [250, 100],  # 맨 위 (바깥)
    [285, 200],  # (안쪽)
    [390, 200],  # 오른쪽 (바깥)
    [305, 265],  # (안쪽)
    [340, 370],  # 오른쪽 아래 (바깥)
    [250, 310],  # (안쪽)
    [160, 370],  # 왼쪽 아래 (바깥)
    [195, 265],  # (안쪽)
    [110, 200],  # 왼쪽 (바깥)
    [215, 200]   # (안쪽)
], dtype=np.int32)
cv2.fillPoly(img,[star_pts],COLOR,cv2.LINE_AA)
pts1=np.array([[100,100],[200,100],[100,200]])
pts2=np.array([[200,100],[300,100],[300,200]])
# cv2.polylines(img,[star_pts],True,COLOR,THICKNESS,cv2.LINE_AA)
# cv2.polylines(img,[pts1],True,COLOR,THICKNESS,cv2.LINE_AA)
# cv2.polylines(img,[pts2],True,COLOR,THICKNESS,cv2.LINE_AA)
# cv2.polylines(img,[pts1,pts2],True,COLOR,THICKNESS,cv2.LINE_AA) #속이 빈 다각형
#그릴 위치, 그릴 좌표들, 닫힘여부, 색, 두께, 선 종류
pts3=np.array([[[100,100],[200,300],[100,400]],[[200,300],[300,300],[300,400]]])
# cv2.fillPoly(img,pts3,COLOR,cv2.LINE_AA)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()