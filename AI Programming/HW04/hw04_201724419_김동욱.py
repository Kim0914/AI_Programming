# -*- coding: utf-8 -*- 
def name_5_1_46():
#--------------- start your code ---------------
    file = "Names.txt" # 파일명을 가지고 있는 변수 file에 Names.txt를 할당한다.
    infile = open(file,'r')  # Name.txt파일을 읽기모드로 준비
    listName = [line.rstrip() for line in infile] # listName에 Names.txt파일을 한 줄씩 읽어가며 저장한다.
    infile.close() # 파일을 닫는다

    setName = set(listName) #list형인 listName을 set함수를 통하여 set으로 정의한다.
    in_name = input('Enter a first name to be included: ') # 추가하고 싶은 문자를 키보드로 부터 입력받는다.
    if not in_name in setName: # 입력받은 문자가 setName에 없을때, 즉 존재하지 않는 경우
        setName.add(in_name)  # set 형을 다루기 위한 함수인 add를 이용하여 입력받은 문자열을 set에 추가한다.
        print(in_name + ' is added in Name.txt')
    setName = sorted(setName) # set 형인 setName을 sorted함수를 통해 오름차순 정렬 후 list로 형을 변환한다.

    outfile = open('Names.txt','w') # Names.txt를 읽기모드로 연다. 모든 내용이 사라지지만 setName에 내용 저장됨.
    for i in range(len(setName)): # setName 길이만큼 반복하며
        setName[i] = setName[i] + '\n' # 모든 리스트에 있는 문자열 마지막에 \n을 추가해준다.
    outfile.writelines(setName) # list형태인 setName을 파일에 쓴다.
    outfile.close() # 파일을 닫는다
#--------------- end your code -----------------



def number_6_1_31():
#--------------- start your code ---------------
    while True:   # 무한루프 반복하며
        try:
            num = input('Enter an integer from 1 to 100: ') # 키보드로 부터 num을 입력받는다.
            num = int(num) # 입력받은 문자열 num을 int형변환. 바꾸는 과정에서 형변환 에러가 발생하면 ValueError
            if 1<= num <= 100:  # 주어진 if조건을 만족시키면 
                print('Your number is ' + str(num) + '.') # 결과를 출력하고
                break;   # 무한루프를 탈출한다.
        except ValueError: # 숫자가 아닌 다른 문자열이 입력될 때
            print('You did not enter an integer.')
        else: # if문 조건에 걸리지 않고 else 구문이 실행될 때, 즉 num이 1보다 작고 100보다 큰 경우
            if num < 1 or num > 100:
                print('Your number was not betwwen 1 and 100.')
#--------------- end your code -----------------



def alphabet_6_2_9():
#--------------- start your code ---------------
    import random # 무작위의 값을 추출하기 위해 random을 import한다.
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
    print(random.sample(alpha,3)) # 모든 알파벳을 담은 list alpha를 정의하고, alpha에서 3개의 표본을 랜덤으로 뽑아서 출력한다.
#--------------- end your code -----------------



if __name__ == '__main__':
    name_5_1_46()
    number_6_1_31()
    alphabet_6_2_9()