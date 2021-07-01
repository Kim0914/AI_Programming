'''
Exercise 3.4

66.Median

The median of an ordered set of measurements is a number separating the lower half from the upper half. 
If the number of measurements is odd, the median is the middle measurement. If the number of measurements is even, 
the median is the average of the two middle measurements. 
Write a program that requests a number n and a set of n measurements (not necessarily ordered) as input 
and then displays the median of the measurements.

===================== example =====================
    How many numbers do you want to enter? 4
    Enter a number: 9
    Enter a number: 3
    Enter a number: 6
    Enter a number: 5
    Median: 5.5

===================== sample input =====================
    4 [9,3,6,5]
===================== sample output ====================
    5.5

'''

def median(howMany, listOfNumbers):
    howMany = int(howMany)
    listOfNumbers = listOfNumbers.strip('[]\n')
    listOfNumbers = listOfNumbers.split(',')
    listOfNumbers = list(map(int,listOfNumbers))
    

#--------------- start your code ---------------
    listOfNumbers = sorted(listOfNumbers) # 오름차순으로 정렬
    if howMany % 2 == 0: # list의 갯수가 짝수일 때
        median = (listOfNumbers[int((howMany/2)-1)] + listOfNumbers[int((howMany/2))])/2 # 짝수인 경우 중간 두개의 값 평균을 구한다.
    else: # list의 갯수가 홀수일 때
        median = listOfNumbers[int(howMany/2)] # 홀수인 경우 가운데 index가 가지는 값을 median으로 정의한다.
#--------------- end your code -----------------
    return (median)



'''
78. Special Number

Write a program to find the four-digit number, call it abcd, whose digits are reversed when the number is multiplied by 4. 
That is, 4 x abcd = dcba*.

================= example =================
        Since 4 times 2178 is 8712,
        the special number is 2178.

===================== sample input =====================
    1000 10000
===================== sample output ====================
    2178

'''

def special_number(min, max):
    for i in range (int(min), int(max)):
#--------------- start your code ---------------
        strnum = list(str(i)) # i를 문자열로 변환 후 list로 하나씩 분리한다.
        strnum = strnum[::-1] # [::-1]을 이용하여 list를 거꾸로 뒤집은 후 strnum에 할당한다.
        result = "".join(strnum) # 거꾸로 뒤집은 list를 "".join을 이용해 문자열로 변환한다.
        result = int(result) # 문자열로 변환한 result를 int로 형변환 시킨다.
        if i * 4 == result: # i * 4의 값이 result 즉, dcba로 변환한 값과 같으면
            break           # 반복문을 탈출한다.
#--------------- end your code -----------------
    return (i)



'''
Exercise 4.2

70. Wilson’s Theorem

A number is prime if its only factors are 1 and itself. 
Write a program that determines whether a number is prime by using the theorem "The number n is a prime number 
if and only if n divides (n – 1)! + 1." 
The program should define a Boolean-valued function named isPrime that calls a function named factorial,
and Boolean-valued function named wilson that that calls a function named isPrime.

================= example =================
        Enter an integer greater than 1: 37
        37 is a prime number.

================= sample input =================
    37
================= sample output =================
    True

'''

def wilson(input):
#--------------- start your code ---------------
    num = int(input)          # String형인 input을 int로 형변환 한 후 num에 할당시켜준다.
    return(isPrime(num))     # num을 isPrime 함수의 인자로 전달시켜 소수인지 판단하여 isPrime의 True or False 값을 리턴받는다.  
#--------------- end your code -----------------

def isPrime(n):
#--------------- start your code ---------------
    if factorial(n)%n == 0:     # (n-1)! + 1 값이 n으로 나누어 떨어지면 True, 그렇지 않으면 False
        return True            # 소수이면 True를 리턴하고
    else:
        return False           # 소수가 아니면 False를 리턴한다.
    
#--------------- end your code -----------------


def factorial(n):
    value = 1
#--------------- start your code ---------------
    for i in range(1,n):    # 1부터 n-1까지 반복하며 (n-1)! 값을 계산하여 value에 할당한다.
        value = value * i
    value+=1;               # (n-1)! + 1 을 완성시켜준다.
#--------------- end your code -----------------
    return value




'''
CHAPTER 4 PROGRAMMING PROJECTS

5. Alphabetical Order  

The following words have three consecutive letters that are also consecutive letters in the alphabet: 
THIRSTY, NOPE, AFGHANISTAN, STUDENT. 
Write a program that accepts a word as input and determines whether or not it has three consecutive letters 
that are consecutive letters in the alphabet. 
The program should use a Boolean-valued function named isTripleConsecutive that accepts an entire word as input. 
Hint: Use the ord function.

================= exmaple =================
        Enter a word: HIJACK
        HIJACK contains three successive letters
        in consecutive alphabetical order.
        
================= smaple input =================
    HIJACK
================= smaple output =================
    True

'''

def isTripleConsecutive(word):
#--------------- start your code ---------------
    for i in range(0,len(word)-2):  # 문자 세개씩 비교하므로 마지막 [인덱스 - 2] 까지 반복하면 모든 경우 검사 가능.
        if (ord(word[i])+2) == (ord(word[i+1])+1) and (ord(word[i])+2) == ord(word[i+2]) and (ord(word[i+1])+1) == ord(word[i+2]):
            return True     # 문자의 ascii값을 반환하는 ord함수를 통해 연속된 문자는 ascii값이 1씩 차이나므로 위 조건식으로 판별
        elif i == len(word) - 3: # 마지막 집합을 검사하는 index인 len(word) - 3 까지도 True 조건을 만족하지 못한 경우
            return False
#--------------- end your code -----------------
def alphabetical_order(input):
#--------------- start your code ---------------
    info = input.lower()    # 입력받은 문자열을 모두 소문자로 변환한다.
    info = list(info)       # 글자 하나당 비교하기 위해 lnfo를 list로 변환한다.
    return(isTripleConsecutive(info))  # isTripleConsecutive에 list형인 info를 인자로 전달하여 isTripleConsecutive의 리턴값을 리턴한다.
#--------------- end your code -----------------






