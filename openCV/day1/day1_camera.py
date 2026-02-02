import cv2
cap=cv2.VideoCapture(0) #0은 기본 카메라 장치 번호
if not cap.isOpened():
    print('카메라 열기 실패')
    exit()

while True:
    ret,frame=cap.read()
    if not ret:
        print('프레임 읽기 실패')
        break
    cv2.imshow('Camera',frame)
    if cv2.waitKey(1) == ord('q'):
        print('사용자 입력에 의해 종료')
        break
cap.release()
cv2.destroyAllWindows()