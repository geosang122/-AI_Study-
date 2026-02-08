## openCV에서 사용하는 글꼴 종류
'''
cv2.FONT_HERSHEY_SIMPLEX           보통 굵기의 산세리프체
cv2.FONT_HERSHEY_PLAIN             얇은 산세리프체
cv2.FONT_HERSHEY_SCRIPT_SIMPLEX    필기체
cv2.FONT_HERSHEY_TRIPLEX           굵은 산세리프체
cv2.FONT_HERSHEY_ITALIC            보통 굵기의 산세리프체 (이탤릭체)
'''

import numpy as np
import cv2

img=np.zeros((512,512,3), dtype=np.uint8)

SCALE=1
COLOR=(255,255,255)
THICKNESS=1

cv2.putText(img, "sanghyun SIMPLEX",(20,50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "sanghyun PLAIN",(20,150), cv2.FONT_HERSHEY_PLAIN, SCALE, COLOR, THICKNESS)
cv2.putText(img, "sanghyun SCRIPT_SIMPLEX",(20,250), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "sanghyun TRIPLEX",(20,350), cv2.FONT_HERSHEY_TRIPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "sanghyun TRIPLEX_ITALIC",(20,450), cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC, SCALE, COLOR, THICKNESS)                 

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()