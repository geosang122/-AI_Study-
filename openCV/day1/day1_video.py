## 동영상 파일 출력
import cv2
cap=cv2.VideoCapture('cat.mp4')

while cap.isOpened(): #파일이 열렸는지?
    ret,frame=cap.read() #프레임 읽기 ret: 읽기 성공여부, frame: 읽은 프레임
    if not ret:
        print('더 이상 프레임이 없습니다.')
        break
    cv2.imshow('video', frame)

    if cv2.waitKey(250) == ord('q'):
        print('사용자 입력에 의해 종료')
        break

cap.release()
cv2.destroyAllWindows()