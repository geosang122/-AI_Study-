#이미지 저장
import cv2
img=cv2.imread("openCV\cat.jpg",cv2.IMREAD_GRAYSCALE) #흑백으로 불러오기
'''
cv2.imshow("cat",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
result=cv2.imwrite("openCV\cat_gray.jpg",img) #이미지 저장
#result=cv2.imwrite("openCV\cat_gray.png",img) png이미지 저장
print("저장여부:",result)

#동영상저장
cap=cv2.VideoCapture('openCV\cat.mp4')

#코덱정의
fourcc=cv2.VideoWriter_fourcc(*'DIVX') #'D' 'I' 'V' 'X'

#프레임크기,fps
width=round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps=cap.get(cv2.CAP_PROP_FPS) *2 #재생속도 2배

out=cv2.VideoWriter('openCV\cat_output_fast.avi',fourcc,fps,(width,height))
#저장파일명, 코덱, fps, 프레임크기(width,height)

while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break
    out.write(frame)
    cv2.imshow("video",frame)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()