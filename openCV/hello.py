import cv2

# OpenCV 버전 출력
print("OpenCV Version:", cv2.__version__)

# 간단한 검은색 이미지 윈도우 띄우기 (Numpy 필요할 수 있음)
import numpy as np

# 300x300 크기의 검은색 이미지 생성 (가로, 세로, 3채널)
img = np.zeros((300, 300, 3), np.uint8)

# 이미지 띄우기
cv2.imshow('Test Window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
