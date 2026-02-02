import cv2

print(cv2.__version__)

#1. 이미지 출력
img = cv2.imread('cat.jpg') #해당경로 파일 읽어오기
cv2.imshow('Cat Image',img) #cat image라는 이름의 창에 img를 표시
key=cv2.waitKey(0) #키 입력 대기 (0: 무한대기)
cv2.destroyAllWindows() #모든 창 닫기
print(key) #눌린 키의 아스키 코드 출력

''' 
읽기옵션
1. cv2.IMREAD_COLOR : 컬러 이미지로 읽기 (기본값)
2. cv2.IMREAD_GRAYSCALE : 흑백 이미지로 읽기
3. cv2.IMREAD_UNCHANGED : 알파 채널 포함 모든 채널 읽기
'''

img_color=cv2.imread('cat.jpg',cv2.IMREAD_COLOR)
img_grayscale=cv2.imread('cat.jpg',cv2.IMREAD_GRAYSCALE)
img_unchanged=cv2.imread('cat.jpg',cv2.IMREAD_UNCHANGED)
cv2.imshow('Cat Color Image',img_color)
cv2.imshow('Cat Grayscale Image',img_grayscale)
cv2.imshow('Cat Unchanged Image',img_unchanged)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
shape
height, widht, channel정보 출력
'''
img=cv2.imread('cat.jpg')
print(img.shape)