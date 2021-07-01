import random
import math

from Setup import * 

class Problem(Setup):
    def __init__(self):
        Setup.__init__(self)
        
        
    #  Numeric, Tsp 클래스에서 오버라이딩 하기 위한 함수 선언
    def setVaraibles(self, parameters):
        Setup.setvariables(parameter)
        self._pFileName = parameters['pFileName']
        
    def describe(self):
        print('Overridding Describe Function')
    
    def report(self):
        print('Overridding Report Function')
      
    def randomInit(self):
        print('Overridding RandomInit Function')
        
    def getDelta(self):
        print('Overridding getDelta Function')
    
    def getLimit(self):
        print('Overridding getLimit Function')
        
    def randomMutant(self, current):
        print('Overridding randomMutant Function')
    
    def mutants(self,current):
        print('Overridding mutants Function')
        
    def setSolution(self, current): # 각 알고리즘에서 계산한 가장 적절한 해를 할당하는 함수
        self._solution = current
        
    def setMinimum(self,valueC):    # 각 알고리즘에서 계산한 최소값을 할당하는 함수
        self._minimum = valueC
    
    def getSolution(self):
        return self._solution
    
    def getValue(self):
        return self._minimum
    
    def getNumEval(self):
        return self._NumEval
    
    def getAvgWhen(self):
        return self._avgWhen

    
    def storeExpResult(self,results):
        self._bestSolution = results[0]
        self._bestMinimum = results[1]
        self._avgMinimum = results[2]
        self._avgNumEval = results[3]
        self._sumOfNumEval = results[4]
        self._avgWhen = results[5]

##############################################################################################
class Numeric(Problem):
    def __init__ (self):
        # 객체에 할당될 변수 초기화하기
        Problem.__init__(self)
        self._NumEval = 0       # 실행 횟수를 할당하기 위한 변수 초기화
        self._expression = []   # 다항식을 할당하기 위한 변수 초기화
        self._domain = []       # 변수와 lower-bound, upper-bound를 할당하기 위한 변수 초기화
        self._LIMIT_STUCK = 100 # LIMIT_STUCK 변수 값 초기화
        self._solution = []     # 계산한 해를 할당하기 위한 변수 초기화
        self._minimum = 0      # 계산한 최소값을 할당하기 위한 변수 초기화
        self._count = 0
    
    def getDelta(self):  # Delta값을 할당하고 리턴해주는 getDelta 함수
        self._DELTA = 0.01
        return self._DELTA
    
    def getLimit(self):  # LIMIT_STUCK값을 할당하고 리턴해주는 getLimit 함수
        self._LIMIT_STUCK = 100
        return self._LIMIT_STUCK
    
    def getAlpha(self):  # Alpha값을 할당하고 리턴해주는 getAlpha 함수
        self._Alpha = 0.01
        return self._Alpha
    
    def getDx(self):    #Dx값을 할당하고 리턴해주는 getDx 함수
        self._dx = 10**(-4)
        return self._dx
    
    def setSolution(self, current): # 각 알고리즘에서 계산한 가장 적절한 해를 할당하는 함수
        self._solution = current
        
    def setMinimum(self,valueC):    # 각 알고리즘에서 계산한 최소값을 할당하는 함수
        self._minimum = valueC
       
         
    def setVariables(self, parameters):
        Problem.setVariables(self,parameters)
        infile = open(self._pFileName,'r')      # open을 이용하여 file을 읽기모드로 읽는다.
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
        
        self._expression = expression
        self._domain = domain
    
    def randomInit(self): 
        ###
        init = [] # 임의의값을 저장하기 위한 list형 init을 초기화 한다.
        
        for i in range(len(self._domain[1])): # 변수들의 갯수 반큼 반복한다.
            init.append(random.randint(self._domain[1][i],self._domain[2][i])) # 각 변수들의 lower-bound와 upper-bound 사이의 임의의 값을 list에 저장

        ###
   
        return init    # Return a random initial point
                       # as a list of values
    
    def randomMutant(self, current): 
        ###

        i = random.randint(0,len(self._domain[0])-1) # 0번째 index부터 마지막 index까지 임의의 값을 할당받는다.

        flag = random.randint(0,1) # 0과 1중 임의의 값을 할당받고,

        if flag == 0:    # 0을 할당받은 경우 d = -DELTA (-0.01)
            d = -self.getDelta()
        else:            # 1을 할당받은 경우 d = DELTA (+0.01)
            d = self.getDelta()

        ###
        return self.mutate(current, i, d) # Return a random successor
     
    def mutants(self,current):  # Steepest Algorithm
        ###
        neighbors = []  # neighbors를 담을 리스트를 초기화 한다.

        for i in range(len(self._domain[0])): # 미지수의 개수만큼 반복하며
            neighbors.append((self.mutate(current,i,-self.getDelta())))  # d가 -1 인경우를 neighbors에 append 한다.
            neighbors.append((self.mutate(current,i,self.getDelta())))   # d가 +1 인경우를 neighbors에 append 한다.
        ###
    
        return neighbors     # Return a set of successors
    
    def mutate(self, current, i, d): ## Mutate i-th of 'current' if legal
        curCopy = current[:]
        l = self._domain[1][i]     # Lower bound of i-th
        u = self._domain[2][i]     # Upper bound of i-th
        if l <= (curCopy[i] + d) <= u:
            curCopy[i] += d
        return curCopy
    
    def evaluate(self,current):
        ## Evaluate the expression of 'p' after assigning
        ## the values of 'current' to the variables
        global NumEval

        self._NumEval += 1
        expr = self._expression         # p[0] is function expression
        varNames = self._domain[0]        # p[1] is domain: [varNames, low, up]
    
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i])
            exec(assignment)
            
        return eval(expr)
    
    
    def takeStep(self, current):
        
        i = random.randint(0,len(self._domain[0])-1)          # 바꾸기 위한 index를 랜덤하게 할당받는다.
        sub = self.getAlpha() * self.gradient(i,current)       # nextP를 구하기 위해 이전 x 에서 빼주기 위한 값, sub를 정의한다.
        current[i] = current[i] - sub   # 각 current에서 sub만큼 빼준다.
        
        return current
   

    def gradient(self, i, current):   # gradient을 계산하는 함수
        
        cp_current = current[:]                       # 평균기울기를 구하기 위한 x = current, x` = cp_current
        cp_current[i] = cp_current[i] + self.getDx()  # takeStep에서 할당받은 index에 dx값을 더해준다.
        
        value = self.evaluate(current)              #f(x) 즉, current를 evaluate 인자로 넘겨 y 값 계산.
        other_value = self.evaluate(cp_current)     #f(x+getDx), 즉 cp_current를 evaluate 인자로 넘겨 y`값 계산.
        
        grad = (other_value - value) / self.getDx()    # 평균기울기 dy(y`-y)/dx 를 계산하여 grad에 할당한다.
        
        return grad
        
    
    def isLegal(self,successor):
        # nextP가 low - upp 범위 안에 있는지?
        judge = True       # boolean 판단을 하기위한 변수 초기화
        
        for i in range(len(successor)):
            l = self._domain[1][i]     # Lower bound of i-th
            u = self._domain[2][i]     # Upper bound of i-th
            if l <= successor[i] <= u:   # 만약 변수들의 범위가 lower , upper 사이에 있으면 True
                judge = True
            else:
                judge = False           # 범위 밖이면 False 할당 후 반복문 탈출
                break
                
        return judge
    
    def describe(self):
        print()
        print("Objective function:")
        print(self._expression)   # Expression
        print("Search space:")
        varNames = self._domain[0] # self._domain = [ [Variables], [Lower bound], [Upper bound] ]
        low = self._domain[1]
        up = self._domain[2]
        for i in range(len(varNames)): # 미지수의 개수만큼 반복
            print(" " + varNames[i] + ":", (low[i], up[i])) 
        
        
    def report(self):
        print('Average objective value: {0:,.3f}'.format(self._avgMinimum))
        print('Average number of evaluations: {0:,}'.format(self._avgNumEval))
        print()
        print("Best Solution found:")
        print(self.coordinate(self._bestSolution))  # Convert list to tuple , current
        print("Best value: {0:,.3f}".format(self._bestMinimum)) # valueC
        print()
        print("Total number of evaluations: {0:,}".format(self._sumOfNumEval))
        
    def coordinate(self,solution):
        c = [round(value, 3) for value in solution]
        return tuple(c)  # Convert the list to a tuple

    def initializePop(self, size): # Make a population of given size
        pop = []
        for i in range(size):
            chromosome = self.randBinStr()
            pop.append([0, chromosome])
        return pop

    def randBinStr(self):
        k = len(self._domain[0]) * self._resolution
        chromosome = []
        for i in range(k):
            allele = random.randint(0, 1)
            chromosome.append(allele)
            print(chromosome)
        return chromosome

    def evalInd(self, ind):  # ind: [fitness, chromosome]
        ind[0] = self.evaluate(self.decode(ind[1])) # Record fitness

    def decode(self, chromosome):
        r = self._resolution
        low = self._domain[1]  # list of lower bounds
        up = self._domain[2]   # list of upper bounds
        genotype = chromosome[:]
        phenotype = []
        start = 0
        end = r   # The following loop repeats for # variables
        for var in range(len(self._domain[0])): 
            value = self.binaryToDecimal(genotype[start:end],
                                         low[var], up[var])
            phenotype.append(value)
            start += r
            end += r
        return phenotype

    def binaryToDecimal(self, binCode, l, u):
        r = len(binCode)
        decimalValue = 0
        for i in range(r):
            decimalValue += binCode[i] * (2 ** (r - 1 - i))
        return l + (u - l) * decimalValue / 2 ** r

    def crossover(self, ind1, ind2, uXp):
        # pC is interpreted as uXp# (probability of swap)
        chr1, chr2 = self.uXover(ind1[1], ind2[1], uXp)
        return [0, chr1], [0, chr2]

    def uXover(self, chrInd1, chrInd2, uXp): # uniform crossover
        chr1 = chrInd1[:]  # Make copies
        chr2 = chrInd2[:]
        for i in range(len(chr1)): 
            if random.uniform(0, 1) < uXp:
                chr1[i], chr2[i] = chr2[i], chr1[i]
        return chr1, chr2

    def mutation(self, ind, mrF):  # bit-flip mutation
        # pM is interpreted as mrF (factor to adjust mutation rate)
        child = ind[:]    # Make copy
        n = len(ind[1])
        for i in range(n):
            if random.uniform(0, 1) < mrF * (1 / n):
                child[1][i] = 1 - child[1][i]
        return child

    def indToSol(self, ind):
        return self.decode(ind[1])
    
##############################################################################################

class Tsp(Problem):
    def __init__(self):
        Problem.__init__(self)
        # 객체에 할당될 변수 초기화하기
        self._NumEval = 0   
        self._LIMIT_STUCK = 100
        self._numCities = 0   # 파일에서 읽은 총 city의 수를 할당받을 변수를 초기화한다.
        self._locations = []   # 좌표를 할당받을 변수를 초기화 한다.
        self._table = []     # 좌표간의 이동거리를 계산하기 위한 변수를 초기화 한다.
        self._cost = 0       # 비용 cost를 0으로 초기화 한다.
        self._solution = []  # 적절한 해를 할당받을 변수를 초기화 한다.
        self._minimum = 0   # 최소값을 할당받을 변수를 초기화 한다.
        self._count = 0
        
      
    def setSolution(self, current):   # 각 알고리즘에서 계산한 가장 적절한 해를 할당하는 함수
        self._solution = current
        
    def setMinimum(self,valueC):    # 각 알고리즘에서 계산한 최소값을 할당하는 함수
        self._minimum = valueC
    
    def getLimit(self):            # LIMIT_STUCK값을 할당하고 리턴해주는 getLimit 함수
        self._LIMIT_STUCK = 100
        return self._LIMIT_STUCK
        
    def setVariables(self, parameters):
        Problem.setVariables(self,parameters)
        infile = open(self._pFileName,'r')      # open을 이용하여 file을 읽기모드로 읽는다.
        # First line is number of cities
        self._numCities = int(infile.readline())
        
        line = infile.readline()  # The rest of the lines are locations
        while line != '':
            self._locations.append(eval(line)) # Make a tuple and append
            line = infile.readline()
        infile.close()
        self._table = self.calcDistanceTable(self._numCities, self._locations)
    
    def calcDistanceTable(self, numCities, locations): 
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
    
    
    def randomInit(self):   # Return a random initial tour
        n    = self._numCities  # n에 총 도시의 개수를 할당하고
        init = list(range(n))  # 리스트로 정의한 후 랜덤으로 initial tour를 반환한다.
        random.shuffle(init)  
        return init
    
    
    def evaluate(self,current): ###
    ## Calculate the tour cost of 'current'
        ## 'p' is a Problem instance
        ## 'current' is a list of city ids
        global NumEval  # NumEval을 전역변수로 선언한다.
        self._NumEval += 1    # 반복할때마다 1씩 더해준다. 즉, 총 반복한 횟수
        self._cost = 0        # cost값을 0으로 초기화 시켜준다
        table = self._table   # 좌표마다 거리값이 계산되어 있는 p[2] 를 table 변수에 할당한다.
        
        for i in range(len(current) - 2): # 한번 반복할때마다 다음번째 변수까지 처리하므로 총 index - 2 만큼 반복하며
            self._cost = self._cost + table[current[i]][current[i+1]] # 좌표를 움직이며 이동한 거리의 값을 계산한다.
        
        return self._cost
    
    def mutants(self,current): # Apply inversion
        n = self._numCities   
        neighbors = []
        count = 0
        triedPairs = []
        while count <= n:  # Pick two random loci for inversion
            i, j = sorted([random.randrange(n) for _ in range(2)])
            if i < j and [i, j] not in triedPairs:
                triedPairs.append([i, j])
                curCopy = self.inversion(current, i, j) # inversion함수를 호출하기 위해 self.을 이용
                count += 1
                neighbors.append(curCopy)
        return neighbors
    
    def randomMutant(self,current): # Apply inversion
        while True:
            i, j = sorted([random.randrange(self._numCities)
                           for _ in range(2)])
            if i < j:
                curCopy = self.inversion(current, i, j)  # inversion함수를 호출하기 위해 self.을 이용
                break
        return curCopy

    def inversion(self,current, i, j):  # Perform inversionj
        curCopy = current[:]
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
            i += 1
            j -= 1
        return curCopy

    def describe(self):
        n = self._numCities
        print()
        print("Number of cities:", n)
        print("City locations:")
        locations = self._locations
        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end = '')
            if i % 5 == 4:
                print()
                
    def report(self):
        print('Average objective value: {0:,.3f}'.format(self._avgMinimum))
        print('Average number of evaluations: {0:,}'.format(self._avgNumEval))
        print()
        print("Best order of visits:")
        self.tenPerRow(self._solution)       # Print 10 cities per row
        print("Minimum tour cost: {0:,}".format(round(self._minimum)))
        print()
        print("Total number of evaluations: {0:,}".format(self._sumOfNumEval))
        
        
    def tenPerRow(self,solution):
        for i in range(len(solution)):
            print("{0:>5}".format(solution[i]), end='')
            if i % 10 == 9:
                print()

    def initializePop(self, size): # Make a population of given size
        n = self._numCities        # n: number of cities
        pop = []
        for i in range(size):
            chromosome = self.randomInit()
            pop.append([0, chromosome])
        return pop

    def evalInd(self, ind):  # ind: [fitness, chromosome]
        ind[0] = self.evaluate(ind[1]) # Record fitness

    def crossover(self, ind1, ind2, XR): 
        # pC is interpreted as XR (crossover rate)
        if random.uniform(0, 1) <= XR:
            chr1, chr2 = self.oXover(ind1[1], ind2[1])
        else:
            chr1, chr2 = ind1[1][:], ind2[1][:]  # No change
        return [0, chr1], [0, chr2]

    def oXover(self, chrInd1, chrInd2):  # Ordered Crossover
        chr1 = chrInd1[:]
        chr2 = chrInd2[:]  # Make copies
        size = len(chr1)
        a, b = sorted([random.randrange(size) for _ in range(2)])
        holes1, holes2 = [True] * size, [True] * size
        for i in range(size):
            if i < a or i > b:
                holes1[chr2[i]] = False
                holes2[chr1[i]] = False
        # We must keep the original values somewhere
        # before scrambling everything
        temp1, temp2 = chr1, chr2
        k1, k2 = b + 1, b + 1
        for i in range(size):
            if not holes1[temp1[(i + b + 1) % size]]:
                chr1[k1 % size] = temp1[(i + b + 1) % size]
                k1 += 1
            if not holes2[temp2[(i + b + 1) % size]]:
                chr2[k2 % size] = temp2[(i + b + 1) % size]
                k2 += 1
        # Swap the content between a and b (included)
        for i in range(a, b + 1):
            chr1[i], chr2[i] = chr2[i], chr1[i]
        return chr1, chr2

    def mutation(self, ind, mR): # mutation by inversion
        # pM is interpreted as mR (mutation rate for inversion)
        child = ind[:]  # Make copy
        if random.uniform(0, 1) <= mR:
            i, j = sorted([random.randrange(self._numCities)
                           for _ in range(2)])
            child[1] = self.inversion(child[1], i, j)
        return child

    def indToSol(self, ind):
        return ind[1]   