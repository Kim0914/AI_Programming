from Setup import *
import random
import math
from numpy import random

class Optimizer(Setup):
    def __init__(self):
        self._limitStuck = 1000
        self._numRestart = 0
        
    def setVariables(self,parameters): # 각각 알고리즘의 algorithm type과 problem type을 할당하는 함수.
        Setup.setVariables(self,parameters)
        self._pType = parameters['pType']
        self._numExp = parameters['numExp']
        self._numRestart = parameters['numRestart']
       
        
    
    def displaySetting(self):  # Problem에 따라 다르기 때문에 오버라이딩 해야함
        if self._pType == 1:           # Numeric Optimization
            print('Mutation step size:', self._delta)
        elif self._pType == 2:         # Tsp Optimization
            print()
            
    def run(self):  # 알고리즘에서 각각 오버라이딩 하기 위해 선언한 run 함수
        pass
    
        
    def getNumExp(self):
        return self._numExp   # numExp를 반환하기 위해 선언한 함수
    
    def displayNumExp(self):
        print()
        print('Number of experiments:', self._numExp)
        
#####################################################################################################################################
class HillClimbing(Optimizer):
    
    def __init__(self):
        Optimizer.__init__(self)
        
    def randomRestart(self,p):
        i = 1
        self.run(p)   # 초기값을 설정하기 위해 self.run(p)을 한번 실행해준다.
        bestSolution = p.getSolution()
        bestMinimum = p.getValue()    # First result is current best
        numEval = p.getNumEval()
        
        while i < self._numRestart:
            self.run(p)
            newSolution = p.getSolution()
            newMinimum = p.getValue()
            numEval += p.getNumEval()
            
            if newMinimum < bestMinimum:
                bestSolution = newSolution
                bestMinimum = newMinimum
            i+=1
        
        p.setSolution(bestSolution)
        p.setMinimum(bestMinimum)
        
#####################################################################################################################################
class MetaHeuristics(Optimizer):
    def __init__(self):
        Optimizer.__init__(self)
        self._limitEval = 0
        self._whenBest = 0
        
    def setVariables(self,parameters):
        Optimizer.setVariables(self,parameters)
        self._limitEval = parameters['limitEval']
        self._popSize = parameters['popSize']
        self._resolution = parameters['resolution']
        self._uXp = parameters['uXp']
        self._mrF = parameters['mrF']
        self._XR = parameters['XR']
        self._mR = parameters['mR']
        
    def getWhenBestFound(self):        
        return self._whenBest
     
    def displaySetting(self):
        Optimizer.displaySetting(self)
        print('Total number of evaluations until temination : ', self._limitEval)
        print()
#####################################################################################################################################
class SteepestAscent(HillClimbing):
    
    def __init__(self):
        HillClimbing.__init__(self)       # HillClimbing Class의 속성과 super class인 Setup Class의 속성을 상속한다.
        
        
    def displaySetting(self):
        if self._pType == 1:           # Numeric Optimization
            print()           
            print("Search algorithm: Steepest-Ascent Hill Climbing")
            print()
            print('Number of random restarts: ', self._numRestart)
            print()
            print('Mutation step size:', self._delta)   # Setup Class에서 초기화한 self._delta변수 사용
            print('Max evaluations with no improvement: {}'.format(self._limitStuck), end='')
            print(' iterations')
            print()
            
        elif self._pType == 2:         # Tsp Optimization
            print()
            print("Search algorithm: Steepest-Ascent Hill Climbing")
            print()
            print('Number of random restarts: ', self._numRestart)
            print()
            print('Max evaluations with no improvement: {}'.format(self._limitStuck), end='')
            print(' iterations')
            print()
        
        
    def setVariables(self, aType, pType):
        self._aType = aType
        self._pType = pType
   
        
    def run(self,p):
        current = p.randomInit() # 'current' is a list of values
        valueC = p.evaluate(current)
        f = open('Steepest.txt', 'w')
        while True:
            f.write(str(valueC) + '\n')
            neighbors = p.mutants(current)   # 생성된 객체 p를 통해 p.mutant(current) 함수를 호출하여 돌연변이 생성.
            successor, valueS = self.bestOf(neighbors, p)
            
            if valueS >= valueC: 
                break
            else:
                current = successor
                valueC = valueS
        p.setSolution(current) # 생성된 객체 p를 통해 p.setSolution 함수를 호출한다.
        p.setMinimum(valueC) # 생성된 객체 p를 통해 p.setMinimum 함수를 호출한다.
        f.close()
        
    def bestOf(self, neighbors, p):
        bestValue = p.evaluate(neighbors[0]) # bestValue를 생성된 객체 p를 통해 p.evaluate(neighbors[0]) 값으로 초기화 한다.
        best = neighbors[0]                 # best를 neighbors의 첫번째 리스트 값으로 초기화 한다.
        for i in range(len(neighbors)):    # neighbors의 길이 만큼 반복하며
            if p.evaluate(neighbors[i]) < bestValue:   # i번째 인덱스의 p.evaluate(neighbors[i]) 값이 bestValue보다 작으면
                bestValue = p.evaluate(neighbors[i])   # 즉, 더 작은 값이면 bestValue 를 p.evaluate(neighbors[i])로 변경하고
                best = neighbors[i]                    # best 를 neighbors[i]로 변경한다.
        return best, bestValue
    

#####################################################################################################################################
class FirstChoice(HillClimbing):
    
    def __init__(self):
        HillClimbing.__init__(self)     # HillClimbing Class의 속성과 super class인 Setup Class의 속성을 상속한다.
        
    def displaySetting(self):
        if self._pType == 1:           # Numeric Optimization
            print()
            print("Search algorithm: First-Choice Hill Climbing")
            print()
            print('Number of random restarts: ', self._numRestart)
            print()
            print('Mutation step size:', self._delta)   # Setup Class에서 초기화한 self._delta변수 사용
            print('Max evaluations with no improvement: {}'.format(self._limitStuck), end='')
            print(' iterations')
            print()
            
        elif self._pType == 2:         # Tsp Optimization
            print()
            print("Search algorithm: First-Choice Hill Climbing")
            print()
            print('Number of random restarts: ', self._numRestart)
            print()
            print('Max evaluations with no improvement: {}'.format(self._limitStuck), end='')
            print(' iterations')
            print()
                
    def run(self,p):
        current = p.randomInit()   # 생성된 객체 p를 통해 randomInit()함수를 호출 'current' is a list of values
        valueC = p.evaluate(current) # 생성된 객체 p를 통해 evalutate()함수를 호출
        i = 0
        f = open('first.txt', 'w')
        
        while i < self._limitStuck: # Hilliclimbing Class에서 초기화한 self._limitStuck 변수 사용.
            f.write(str(valueC) + '\n')
            successor = p.randomMutant(current) # 생성된 객체 p를 통해 randomMutant()함수를 호출
            valueS = p.evaluate(successor) # 생성된 객체 p를 통해 evalutate()함수를 호출
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0              # Reset stuck counter
            else:
                i += 1
        f.close()
      
        p.setSolution(current) # 생성된 객체 p를 통해 setSolution()함수를 호출
        p.setMinimum(valueC)   # 생성된 객체 p를 통해 setMinimum()함수를 호출
        
#####################################################################################################################################    

class GradientDescent(HillClimbing):
    
    def __init__(self):   
        HillClimbing.__init__(self)   # HillClimbing Class의 속성과 super class인 Setup Class의 속성을 상속한다.
        
    def displaySetting(self):
        print()
        print("Search algorithm: Gradient Descent")
        print()
        print('Number of random restarts: ', self._numRestart)
        print()
        print("Update rate:", self._alpha)  # Setup Class에서 초기화한 self._alpha변수 사용
        print("Increment for calculating derivatives: ", self._dx)  # Setup Class에서 초기화한 self._dx변수 사용
        print('Max evaluations with no improvement: {}'.format(self._limitStuck), end='')
        print(' iterations')
        print()
           
    def run(self,p):
        currentP = p.randomInit()   # 생성된 객체 p를 통해 randomInit함수를 호출한다. # 'currentP' is a list of values
        valueC = p.evaluate(currentP) # 생성된 객체 p를 통해 evaluate함수를 호출한다.
        f = open('Gradient.txt', 'w')
        
        i = 0
        while i < self._limitStuck: # Hilliclimbing Class에서 초기화한 self._limitStuck 변수 사용.
            f.write(str(valueC) + '\n')
            successor = p.takeStep(currentP)  # 생성된 객체 p를 통해 takeStep함수를 호출한다.
            valueN = p.evaluate(successor)  # 생성된 객체 p를 통해 evaluate함수를 호출한다.
            if p.isLegal(successor):  # 생성된 객체 p를 통해 isLegal함수를 호출하여 successor가 범위 내에 있는지 판단한다.
                if valueN < valueC:
                    currentP = successor
                    valueC = valueN
                    i = 0              # Reset stuck counter
                else:
                    i += 1
            else:
                 break
        p.setSolution(currentP) # 생성된 객체 p를 통해 setSolution 함수를 호출한다.
        p.setMinimum(valueC)   # 생성된 객체 p를 통해 setMinimum 함수를 호출한다.
        f.close()

#####################################################################################################################################

class Stochastic(HillClimbing):
    
    def __init__(self):   
        HillClimbing.__init__(self)   # HillClimbing Class의 속성과 super class인 Setup Class의 속성을 상속한다.
        
    def displaySetting(self):
        if self._pType == 1:           # Numeric Optimization
            print()
            print("Search algorithm: Stochastic Algorithm")
            print()
            print('Number of random restarts: ', self._numRestart)
            print()
            print('Mutation step size:', self._delta)   # Setup Class에서 초기화한 self._delta변수 사용
            print('Max evaluations with no improvement: {}'.format(self._limitStuck), end='')
            print(' iterations')
            print()
            
        elif self._pType == 2:         # Tsp Optimization
            print()
            print("Search algorithm: Stochastic Algorithm")
            print()
            print('Number of random restarts: ', self._numRestart)
            print()
            print('Max evaluations with no improvement: {}'.format(self._limitStuck), end='')
            print(' iterations')
            print()
        
        
    def run(self,p):
        current = p.randomInit() # 'current' is a list of values
        valueC = p.evaluate(current)
        f = open('Stochastic.txt', 'w')
        
        while True:
            f.write(str(valueC) + '\n')
            neighbors = p.mutants(current)   # 생성된 객체 p를 통해 p.mutant(current) 함수를 호출하여 돌연변이 생성.
            successor, valueS = self.stochasticBest(neighbors, p) # 같은 클래스에 선언된 stochasticBest함수를 호출하여 값을 반환받음
            
            if valueS >= valueC: 
                break
            else:
                current = successor
                valueC = valueS
        p.setSolution(current) # 생성된 객체 p를 통해 p.setSolution 함수를 호출한다.
        p.setMinimum(valueC) # 생성된 객체 p를 통해 p.setMinimum 함수를 호출한다.
        f.close()
        
    def stochasticBest(self, neighbors, p):
        # Smaller valuse are better in the following list
        valuesForMin = [p.evaluate(indiv) for indiv in neighbors]
        largeValue = max(valuesForMin) + 1
        valuesForMax = [largeValue - val for val in valuesForMin]
        # Now, larger values are better
        total = sum(valuesForMax)
        randValue = random.uniform(0, total)
        s = valuesForMax[0]
        for i in range(len(valuesForMax)):
            if randValue <= s: # The one with index i is chosen
                break
            else:
                s += valuesForMax[i+1]
        return neighbors[i], valuesForMin[i]


#####################################################################################################################################
class SimulatedAnnealing(MetaHeuristics):
    
    def __inif__(self):
        MetaHeuristics.__init__(self)
        self._numSample = 100
        
        
    def displaySetting(self):
        print()
        print("Search Algorithm: Simulated Annealing")
        print()
        MetaHeuristics.displaySetting(self)
        
    def run(self,p):
        current = p.randomInit()   # current를 랜덤으로 할당받아 초기화한다.
        valueC = p.evaluate(current)  # 할당받은 current를 이용해 초기값 value를 구한다.
        temp = self.initTemp(p)     # 같은 클래스에 있는 initTemp 함수를 이용해 temp의 초기값을 설정한다.
        best, valueBest = current, valueC

        whenBest = i = 1
        f = open('anneal.txt', 'w')
                               
        while True:
            f.write(str(valueC) + '\n')  # 파일에 한개의 value씩 쓰기위해 개행문자를 추가하여 write한다.
            neighbor = p.randomMutant(current)
            valueN = p.evaluate(neighbor)
            i += 1
            temp = self.tSchedule(temp) # temp를 같은 클래스에 있는 tSchdule 함수를 이용해 Schedule화 시켜준다.

            if temp == 0 or i == self._limitEval:
                break

            dE = valueN - valueC

            if dE < 0:
                current = neighbor
                valueC = valueN 

            elif random.uniform(0,1) < math.exp(-dE/temp):
                current = neighbor
                valueC = valueN
            
            if valueC < valueBest:
                (best, valueBest) = (current, valueC)
                whenBest = i
                
                
            
        self._whenBest = whenBest                
        p.setSolution(best) # 생성된 객체 p를 통해 p.setSolution 함수를 호출한다.
        p.setMinimum(valueBest) # 생성된 객체 p를 통해 p.setMinimum 함수를 호출한다.
        
        f.close()
        
          
       
    def initTemp(self, p): # To set initial acceptance probability to 0.5
        diffs = []
        for i in range(self._numSample):
            c0 = p.randomInit()     # A random point
            v0 = p.evaluate(c0)     # Its value
            c1 = p.randomMutant(c0) # A mutant
            v1 = p.evaluate(c1)     # Its value
            diffs.append(abs(v1 - v0))
        dE = sum(diffs) / self._numSample  # Average value difference
        t = dE / math.log(2)        # exp(–dE/t) = 0.5
        
        return t
    
    def getWhenBestFound(self):        
        return self._whenBest
        
    
    def tSchedule(self, t):
        return t * (1 - (1 / 10**4))
        
          
       
    def initTemp(self, p): # To set initial acceptance probability to 0.5
        diffs = []
        for i in range(self._numSample):
            c0 = p.randomInit()     # A random point
            v0 = p.evaluate(c0)     # Its value
            c1 = p.randomMutant(c0) # A mutant
            v1 = p.evaluate(c1)     # Its value
            diffs.append(abs(v1 - v0))
        dE = sum(diffs) / self._numSample  # Average value difference
        t = dE / math.log(2)        # exp(–dE/t) = 0.5
        
        return t
    
    def getWhenBestFound(self):        
        return self._whenBest
        
    
    def tSchedule(self, t):
        return t * (1 - (1 / 10**4))
    
################################################################################################
class GA(MetaHeuristics):
    def __init__(self):
        MetaHeuristics.__init__(self)
        self._popSize = 0     # Population size
        self._uXp = 0   # Probability of swappping a locus for Xover
        self._mrF = 0   # Multiplication factor to 1/n for bit-flip mutation
        self._XR = 0    # Crossover rate for permutation code
        self._mR = 0    # Mutation rate for permutation code
        self._pC = 0    # Probability parameter for Xover
        self._pM = 0    # Probability parameter for mutation

    def setVariables(self, parameters):
        MetaHeuristics.setVariables(self, parameters)
        self._popSize = parameters['popSize']
        self._uXp = parameters['uXp']
        self._mrF = parameters['mrF']
        self._XR = parameters['XR']
        self._mR = parameters['mR']
        
        if self._pType == 1:
            self._pC = self._uXp
            self._pM = self._mrF
        if self._pType == 2:
            self._pC = self._XR
            self._pM = self._mR

    def displaySetting(self):
        print() 
        print("Search Algorithm: Genetic Algorithm")
        print()
        MetaHeuristics.displaySetting(self)
        print()
        print("Population size:", self._popSize)
        if self._pType == 1:   # Numerical optimization
            print("Number of bits for binary encoding:", self._resolution)
            print("Swap probability for uniform crossover:", self._uXp)
            print("Multiplication factor to 1/L for bit-flip mutation:",
                  self._mrF)
        elif self._pType == 2: # TSP
            print("Crossover rate:", self._XR)
            print("Mutation rate:", self._mR)
            
    def run(self,p):
        population = p.initializePop(self._popSize)   # population을 popSize만큼 초기화 한다.
        
        k = 0
        while k < self._limitEval:  # limitEval까지 반복하여 최적의 값을 찾는다.
            new_population = []
            Fn_sum = 0              # 각 individual 들의 Fitness 합을 계산하는 변수 초기화
            for i in range(0,len(population)):
                p.evalInd(population[i])   # 각 개인마다의 Fitness 계산을 한다
                Fn_sum = Fn_sum + population[i][0]  # 총 Fitness의 합을 구한다.
            population.sort(reverse = True)  # population을 Fitness 값을 기준으로 내림차순 정렬
            
            for i in range(0,len(population)):
                x,y = self.randomSelection(population,Fn_sum)  # 확률에 따른 individual을 선택하여
                child_x, child_y = p.crossover(x,y,self._uXp) # 선택된 두 가지의 individual을 crossover한 후
                child = p.mutation(child_x, self._mrF)  # mutation 과정을 거친 child를 리턴 받은 후
                new_population.append(child)               # 새로운 population에 child를 append한다.
            population = new_population             
            k+=1
  
        value = p.indToSol(population[0])  # limitEval만큼 반복 후, 가장 처음에 있는 value를 선택 (오름차순 정렬이기 때문)
        valueBest = p.evaluate(value)   # 그 값들을 evaluate하여 valueBest에 저장
        p.setSolution(value) # 생성된 객체 p를 통해 p.setSolution 함수를 호출한다.
        p.setMinimum(valueBest) # 생성된 객체 p를 통해 p.setMinimum 함수를 호출한다.   
        
        
    def randomSelection(self, population, Fn):
        prob = []    # 개인마다의 확률을 계산하기 위한 prob 변수 설정
        data = []    # 그 개인들의 index를 저장하기 위한 data 변수 설정
        pop = population
        
        for i in range(len(pop)):
            data.append(i)  # data에 index를 append
            prob.append(population[i][0] / Fn)  # 총 Fn의 합으로 나눠진 각각의 Fn 즉, 확률을 prob에 append
        
        x,y = random.choice(data, 2, p=prob, replace = False) # 중복을 허용하지 않고, 확률에 따라 2개의 index를 리턴
        return pop[x],pop[y] # 각각의 인덱스에 해당하는 individual을 리턴한다.