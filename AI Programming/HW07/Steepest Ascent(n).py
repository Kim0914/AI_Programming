from Problem import Numeric

def main():
    p = Numeric()
    p.setVariables()
    steepestAscent(p)
    p.describe()
    displaySetting(p)
    p.report()
    
def steepestAscent(p):
    current = p.randomInit() # 'current' is a list of values
    valueC = p.evaluate(current)
    while True:
        neighbors = p.mutants(current)   # 생성된 객체 p를 통해 p.mutant(current) 함수를 호출하여 돌연변이 생성.
        successor, valueS = bestOf(neighbors, p) 
        if valueS >= valueC: 
            break
        else:
            current = successor
            valueC = valueS
    p.setSolution(current) # 생성된 객체 p를 통해 p.setSolution 함수를 호출한다.
    p.setMinimum(valueC) # 생성된 객체 p를 통해 p.setMinimum 함수를 호출한다.

def bestOf(neighbors, p): ###
    bestValue = p.evaluate(neighbors[0]) # bestValue를 생성된 객체 p를 통해 p.evaluate(neighbors[0]) 값으로 초기화 한다.
    best = neighbors[0]                 # best를 neighbors의 첫번째 리스트 값으로 초기화 한다.
    for i in range(len(neighbors)):    # neighbors의 길이 만큼 반복하며
        if p.evaluate(neighbors[i]) < bestValue:   # i번째 인덱스의 p.evaluate(neighbors[i]) 값이 bestValue보다 작으면
            bestValue = p.evaluate(neighbors[i])   # 즉, 더 작은 값이면 bestValue 를 p.evaluate(neighbors[i])로 변경하고
            best = neighbors[i]                    # best 를 neighbors[i]로 변경한다.
    return best, bestValue

def displaySetting(p):
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", p.getDelta())
    
main()