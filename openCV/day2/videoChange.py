#고정크기 동영상으로 설정
import cv2

cap=cv2.VideoCapture('openCV\cat.mp4')
while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break
    frame_resized=cv2.resize(frame,(400,500)) #고정크기 설정

    cv2.imshow("video",frame_resized)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#고정크기 동영상으로 설정
import cv2

cap=cv2.VideoCapture('openCV\cat.mp4')
while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break
    frame_resized=cv2.resize(frame,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC) #고정크기 설정

    cv2.imshow("video",frame_resized)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()