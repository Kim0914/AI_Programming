import random
import math

LIMIT_STUCK = 100   # Max number of evaluations enduring no improvement
NumEval     = 0     # Total number of evaluations


def main():
    # Create an instance of TSP
    p = createProblem()    # 'p': (numCities, locations, distanceTable)
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)
    
def createProblem():
    ## Read in a TSP (# of cities, locatioins) from a file.
    ## Then, create a problem instance and return it.
    fileName = input("Enter the file name of a TSP: ")
    infile = open(fileName, 'r')
    # First line is number of cities
    numCities = int(infile.readline())
    locations = []
    line = infile.readline()  # The rest of the lines are locations
    while line != '':
        locations.append(eval(line)) # Make a tuple and append
        line = infile.readline()
    infile.close()
    table = calcDistanceTable(numCities, locations)
    return numCities, locations, table


def calcDistanceTable(numCities, locations): 
    ###
    table = []     # 전체 거리 값을 담는 행렬을 정의
    line_table = []  # 하나의 row마다 거리 값을 담는 list를 정의
    for i in range(0,numCities): # 첫번째 row부터 마지막 row까지
        for j in range(0,numCities): # 각 row의 첫번째 entry 부터 마지막 entry 까지 반복하며
            value = math.sqrt(pow(locations[i][0]-locations[j][0],2) + pow(locations[i][1]-locations[j][1],2)) # 두 점사이의 거리 계산
            line_table.append(value) # 하나의 row마다 처리하는 list인 line_table에 거리 value를 apeend.
        table.append(line_table)  # 하나의 row가 가지고 있는 거리를 전체 행렬 table에 append해줌
        line_table = [] # 직전 계산하였던 row의 거리 값들을 비운다.
    
    
    ###
    return table # A symmetric matrix of pairwise distances


def firstChoice(p):
    current = randomInit(p)   # 'current' is a list of city ids
    valueC  = evaluate(current, p)
    i = 0
    while i < LIMIT_STUCK:
        successor = randomMutant(current, p)
        valueS = evaluate(successor, p)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC

def randomInit(p):   # Return a random initial tour
    n    = p[0]
    init = list(range(n))
    random.shuffle(init)
    return init


def evaluate(current, p): ###
## Calculate the tour cost of 'current'
    ## 'p' is a Problem instance
    ## 'current' is a list of city ids
    global NumEval  # NumEval을 전역변수로 선언한다.
    NumEval += 1    # 반복할때마다 1씩 더해준다. 즉, 총 반복한 횟수
    cost = 0       # 비용 cost를 0으로 초기화 한다.
    table = p[2]   # 좌표마다 거리값이 계산되어 있는 p[2] 를 table 변수에 할당한다.
    for i in range(len(current) - 2): # 한번 반복할때마다 다음번째 변수까지 처리하므로 총 index - 2 만큼 반복하며
        cost = cost + table[current[i]][current[i+1]] # 좌표를 움직이며 이동한 거리의 값을 계산한다.
        
    return cost


def randomMutant(current, p): # Apply inversion
    while True:
        i, j = sorted([random.randrange(p[0])
                       for _ in range(2)])
        if i < j:
            curCopy = inversion(current, i, j)
            break
    return curCopy

def inversion(current, i, j):  # Perform inversion
    curCopy = current[:]
    while i < j:
        curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
        i += 1
        j -= 1
    return curCopy


def describeProblem(p):
    print()
    n = p[0]
    print("Number of cities:", n)
    print("City locations:")
    locations = p[1]
    for i in range(n):
        print("{0:>12}".format(str(locations[i])), end = '')
        if i % 5 == 4:
            print()

def displaySetting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")

def displayResult(solution, minimum):
    print()
    print("Best order of visits:")
    tenPerRow(solution)       # Print 10 cities per row
    print("Minimum tour cost: {0:,}".format(round(minimum)))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def tenPerRow(solution):
    for i in range(len(solution)):
        print("{0:>5}".format(solution[i]), end='')
        if i % 10 == 9:
            print()

main()
