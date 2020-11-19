import numpy as np #숫자를 다루는 데이터 용이
import csv #데이터를 읽어옴
f = open('age.csv')
data = csv.reader(f)
next(data) #한 줄 띄운다
data = list(data) #데이터를 리스트에 넣어줌
name='대치1동' #궁금한 지역의 이름을 입력받음
mn=1 #최솟값을 저장할 변수 생성 및 초기화
result_name='' 
#최솟값을 갖는 지역의 이름을 저장할 변수 생성 및 초기화
result=0 #최솟값을 갖는 지역의 이름을 저장할 변수 생성 및 초기화
home=[]#궁금한 곳의 데이터를 집어넣을 리스트 생성
#궁금한 지역의 인구 구조 저장
for row in data:#한줄씩 처리
    if name in row[0]:#지역이 포함된 행 찾기
        areaname = row[0]
        for i in row[3:]:#3번 인덱스 값부터 슬라이딩 0세~
            home.append(int(i)) #입력받은 지역의 데이터를 home에 저장
            hometotal = int(row[2])#그지역의 전체인구
for k in range(len(home)):
    home[k]=(home[k]/hometotal)
#궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역 찾기
for row in data:
    away = []
    for i in row[3:]: #3번 인덱스 값부터 슬라이딩 0세~
        away.append(int(i)) #입력받은 지역의 데이터를 away에 저장
    awaytotal = int(row[2]) #row[2]:지역당 총인구
    for k in range(len(away)):
        away[k]=(away[k]/awaytotal)
    sum = 0
    for j in range(len(away)):
        sum = sum + (home[j]-away[j])**2
    if sum<mn and name not in row[0]:
        mn=sum
        result_name=row[0]
        result=away
#데이터 시각화     
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.rc('font',family='Malgun Gothic')
plt.title(name+'지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(home,label=name)
plt.plot(result, label=result_name)
plt.legend()
plt.show()
