import csv
f = open('201903subway.csv')
data = csv.reader(f)
next(data);next(data) #두 줄 띄우기(값이 두 줄 아래에 있음)
s_in = [0]*24; s_out=[0]*24 #리스트를 24개 만들어줌(24시간)
for row in data:
    row[4:]=map(int,row[4:]) #시간대별 값 추출
    for i in range(24): #24번 반복하기
        s_in[i]+=row[4+i*2]
 #(4열까지 값X, 승차는 짝수마다 있음)
        s_out[i]+=row[5+i*2] 
#(5열까지 값X, 하자도 짝수마다 있음)
f2 = open('202003subway.csv')
data2 = csv.reader(f2)
next(data2);next(data2)
s_in2 = [0]*24; s_out2 = [0]*24
for row in data2:
    row[4:]=map(int,row[4:])
    for i in range(24):
        s_in2[i]+=row[4+i*2]
        s_out2[i]+=row[5+i*2]
f3 = open('202009subway.csv',encoding='UTF8')
data3 = csv.reader(f3)
next(data3);next(data3)
s_in3 = [0]*24; s_out3 = [0]*24
for row in data3:
    row[4:]=map(int,row[4:])
    for i in range(24):
        s_in3[i]+=row[4+i*2]
        s_out3[i]+=row[5+i*2]        
import matplotlib.pyplot as plt
plt.figure(dpi=300)
plt.rc('font', family = 'Malgun Gothic')
plt.title('지하 시간대별 승하차 인원추이(단위1000만명)')
plt.plot(s_in,label='201903승차')
plt.plot(s_out,label='201903하차')
plt.plot(s_in2,label='202003승차')
plt.plot(s_out2,label='202003하차')
plt.plot(s_in3,label='202009승차')
plt.plot(s_out3,label='202009하차')
plt.legend()
plt.xticks(range(24),range(4,28))
plt.show()
