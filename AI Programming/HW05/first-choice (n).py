import random
import math

DELTA = 0.01   # Mutation step size
LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement
NumEval = 0    # Total number of evaluations


def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)


def createProblem(): ###
    file = input('Enter the file name of a function: ') # input명령어를 통해 읽고 싶은 파일 명을 입력받는다.
    infile = open(file,'r')      # open을 이용하여 file을 읽기모드로 읽는다.
    p = [line.rstrip() for line in infile]     # 한줄씩 읽어가며 리스트에 저장한다.
    expression = p[0]      # 다항식(표현식)을 p[0]로 할당한다.
    domain = []           # 최종적으로 list로 만들 domain을 정의한다.
    elem_list = []        # 미지수(x1,x2...)를 저장할 list형 elem_list를 정의한다.
    low_list = []         # lower-bound를 저장할 list형 low_list를 정의한다.
    up_list = []          # upper-bound를 저장할 list형 up_list를 정의한다.
    
    for i in range(len(p)-1):   
        c = p[i+1].split(',')     # 다항식을 제외한 다음항 p[i+1]부터 문자열을 ,를 기준으로 분리하여 c에 할당한다.
        elem_list.append(c[0])   # 분리한 문자열에서 첫번째 index인 c[0]를 elem_list에 저장한다 ( 미지수 )
        low_list.append(float(c[1]))  # 분리한 문자열에서 두번째 index인 c[1]를 float로 형변환 하여 low_list에 저장한다  (lower- bound)
        up_list.append(float(c[2]))   # 분리한 문자열에서 세번째 index인 c[2]를 float로 형변환 하여 up_list에 저장한다 (upper-bound
        
    domain.append(elem_list)
    domain.append(low_list)
    domain.append(up_list)   # list domain에 append를 이용하여  list로 저장된 미지수, lower-bound, upper-bound를 추가한다
    
    return expression, domain


def firstChoice(p):
    current = randomInit(p)   # 'current' is a list of values
    valueC = evaluate(current, p)
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


def randomInit(p): 
    ###
    init = [] # 임의의값을 저장하기 위한 list형 init을 초기화 한다.
   
    for i in range(len(p[1][0])): # 변수들의 갯수 반큼 반복한다.
        init.append(random.randint(p[1][1][i],p[1][2][i])) # 각 변수들의 lower-bound와 upper-bound 사이의 임의의 값을 list에 저장
    
    ###
    return init    # Return a random initial point
                   # as a list of values

def evaluate(current, p):
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables
    global NumEval
    
    NumEval += 1
    expr = p[0]         # p[0] is function expression
    varNames = p[1][0]  # p[1] is domain: [varNames, low, up]
    for i in range(len(varNames)):
        assignment = varNames[i] + '=' + str(current[i])
        exec(assignment)
    return eval(expr)


def randomMutant(current, p): 
    ###
    i = random.randint(0,len(p[1][0])-1) # 0번째 index부터 마지막 index까지 임의의 값을 할당받는다.
    
    flag = random.randint(0,1) # 0과 1중 임의의 값을 할당받고,
    
    if flag == 0:    # 0을 할당받은 경우 d = -DELTA (-0.01)
        d = -DELTA
    else:            # 1을 할당받은 경우 d = DELTA (+0.01)
        d = DELTA
    
    
    
    ###
    return mutate(current, i, d, p) # Return a random successor


def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    curCopy = current[:]
    domain = p[1]        # [VarNames, low, up]
    l = domain[1][i]     # Lower bound of i-th
    u = domain[2][i]     # Upper bound of i-th
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy

def describeProblem(p):
    print()
    print("Objective function:")
    print(p[0])   # Expression
    print("Search space:")
    varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i])) 

def displaySetting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple

main()
