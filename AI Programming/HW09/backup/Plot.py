import matplotlib.pyplot as plt

file = 'first.txt'
infile = open(file,'r')

other_file = 'anneal.txt'
new_infile = open(other_file,'r')

value = [line.rstrip() for line in infile] # 라인마다 한 줄씩 읽어오며 value 리스트에 저장한다.
new_value = [line.rstrip() for line in new_infile] # 라인마다 한 줄씩 읽어오며 value 리스트에 저장한다.



for i in range(len(value)):
    value[i] = round(float(value[i]),0)  # string 값인 value를 int값으로 변환하여 리스트에 저장한다.

for i in range(len(new_value)):
    new_value[i] = round(float(new_value[i]),0)  # string 값인 value를 int값으로 변환하여 리스트에 저장한다.

plt.figure()
plt.plot(value)
plt.plot(new_value)
plt.xlabel('Number Of Evaluations')   # x축의 제목을 설정한다.
plt.ylabel('Tour Cost')               # y축의 제목을 설정한다.
plt.xticks([0,10000,20000,30000,40000,50000]) # x축 단위 바꾸기 
plt.title('Search Perfomance(TSP-100)')  # 그래프의 제목을 설정한다.
plt.legend(['First-Choice HC', 'Simulated Annealing'])  # 그래프에서 범례를 설정한다.
plt.show()