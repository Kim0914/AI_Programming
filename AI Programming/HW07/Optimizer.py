from Setup import *

class HillClimbing(Setup):
    
    def __init__(self):
        Setup.__init__(self)
        self._limitStuck = 100
    
    def setVariables(self, aType, pType): # 각각 알고리즘의 algorithm type과 problem type을 할당하는 함수.
        self._aType = aType
        self._pType = pType
    
    def displaySetting(self):  # Problem에 따라 다르기 때문에 오버라이딩 해야함
        if self._pType == 1:           # Numeric Optimization
            print('Mutation step size:', self._delta)
        elif self._pType == 2:         # Tsp Optimization
             print("Search algorithm: First-Choice Hill Climbing")
            
    def run(self):  # 알고리즘에서 각각 오버라이딩 하기 위해 선언한 run 함수
        pass
    
    def setSolution(self, current): # 각 알고리즘에서 계산한 가장 적절한 해를 할당하는 함수
        self._solution = current
        
    def setMinimum(self,valueC):    # 각 알고리즘에서 계산한 최소값을 할당하는 함수
        self._minimum = valueC
        
#####################################################################################################################################
class SteepestAscent(HillClimbing):
    
    def __init__(self):
        HillClimbing.__init__(self)       # HillClimbing Class의 속성과 super class인 Setup Class의 속성을 상속한다.
        
        
    def displaySetting(self):
        if self._pType == 1:           # Numeric Optimization
            print()
            print('Mutation step size:', self._delta)   # Setup Class에서 초기화한 self._delta변수 사용
            print()
            print("Search algorithm: Steepest-Ascent Hill Climbing")
            
        elif self._pType == 2:         # Tsp Optimization
            print()
            print("Search algorithm: Steepest-Ascent Hill Climbing")
        
        
    def setVariables(self, aType, pType):
        self._aType = aType
        self._pType = pType
   
        
    def run(self,p):
        current = p.randomInit() # 'current' is a list of values
        valueC = p.evaluate(current)
        while True:
            neighbors = p.mutants(current)   # 생성된 객체 p를 통해 p.mutant(current) 함수를 호출하여 돌연변이 생성.
            successor, valueS = self.bestOf(neighbors, p) 
            if valueS >= valueC: 
                break
            else:
                current = successor
                valueC = valueS
        p.setSolution(current) # 생성된 객체 p를 통해 p.setSolution 함수를 호출한다.
        p.setMinimum(valueC) # 생성된 객체 p를 통해 p.setMinimum 함수를 호출한다.

        
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
            print('Mutation step size:', self._delta)   # Setup Class에서 초기화한 self._delta변수 사용
            
        elif self._pType == 2:         # Tsp Optimization
            print()
            print("Search algorithm: First-Choice Hill Climbing")
                
    def run(self,p):
        current = p.randomInit()   # 생성된 객체 p를 통해 randomInit()함수를 호출 'current' is a list of values
        valueC = p.evaluate(current) # 생성된 객체 p를 통해 evalutate()함수를 호출
        i = 0
        while i < self._limitStuck: # Hilliclimbing Class에서 초기화한 self._limitStuck 변수 사용.
            successor = p.randomMutant(current) # 생성된 객체 p를 통해 randomMutant()함수를 호출
            valueS = p.evaluate(successor) # 생성된 객체 p를 통해 evalutate()함수를 호출
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0              # Reset stuck counter
            else:
                i += 1
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
        print("Update rate:", self._alpha)  # Setup Class에서 초기화한 self._alpha변수 사용
        print("Increment for calculating derivatives: ", self._dx)  # Setup Class에서 초기화한 self._dx변수 사용
           
    def run(self,p):
        currentP = p.randomInit()   # 생성된 객체 p를 통해 randomInit함수를 호출한다. # 'currentP' is a list of values
        valueC = p.evaluate(currentP) # 생성된 객체 p를 통해 evaluate함수를 호출한다.

        i = 0
        while i < self._limitStuck: # Hilliclimbing Class에서 초기화한 self._limitStuck 변수 사용.
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

    