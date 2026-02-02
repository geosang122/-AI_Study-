from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
# 1. Linear Regression
''' 
공부 시간(x)에 따른 시험점수(y) 예측하기
'''
dataset= pd.read_csv('LinearRegressionData.csv')
# print(dataset.head())
X=dataset.iloc[:,:-1].values #독립변수 가져오기, row(전체) col(마지막 전까지)
Y=dataset.iloc[:,-1].values #종속변수 가져오기, row(전체) col(마지막)
print(X,Y)
reg=LinearRegression() #객체 생성
reg.fit(X,Y) #학습(모델 생성)
y_pred=reg.predict(X) #X에 대한 예측값
print(y_pred)

# #시각화1
# plt.scatter(X,Y,color='blue') #산점도
# plt.plot(X,y_pred,color='green') #선 그래프
# plt.title('Score by hours')
# plt.xlabel('Hours')
# plt.ylabel('Score')
# plt.show()

print('9시간 공부했을 때 예상 점수', reg.predict([[9]])) #[[9],[8],[7]]
print('회귀계수(기울기):', reg.coef_) #기울기
print('절편:', reg.intercept_) #y절편

#데이터 세트 분리
dataset= pd.read_csv('LinearRegressionData.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0) #train80:test20
# print(X,len(X))
# print(X_train,len(X_train))
# print(X_test,len(X_test))
# print(Y,len(Y))
# print(Y_train,len(Y_train))
# print(Y_test,len(Y_test))

'''
분리된 데이터를 통한 모델링
'''
reg2=LinearRegression()
reg2.fit(X_train,Y_train) #훈련 데이터로 학습

#시각화2-train
plt.scatter(X_train,Y_train,color='blue') #산점도
plt.plot(X_train,reg2.predict(X_train),color='green') #선 그래프
plt.title('Score by hour(train)')
plt.xlabel('Hours')
plt.ylabel('Score')
plt.show()

#시각화3-test
plt.scatter(X_test,Y_test,color='blue') #산점도
plt.plot(X_train,reg2.predict(X_train),color='green') #선 그래프
plt.title('Score by hours(test)')
plt.xlabel('Hours')
plt.ylabel('Score')
plt.show()
###모델 평가
print('(train)모델 평가:', reg2.score(X_train,Y_train))
print('(test)모델 평가:', reg2.score(X_test,Y_test))