from Problem import Numeric


def main():
    p = Numeric()
    p.setVariables()
    firstChoice(p)
    p.describe()
    displaySetting(p)
    p.report()
    
    
    
def firstChoice(p):
    current = p.randomInit()   # 생성된 객체 p를 통해 randomInit()함수를 호출 'current' is a list of values
    valueC = p.evaluate(current) # 생성된 객체 p를 통해 evalutate()함수를 호출
    i = 0
    while i < p.getLimit(): # 생성된 객체 p를 통해 LIMIT_STUCK을 반환하는 getLimit()함수를 호출
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
    
def displaySetting(p):
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", p.getDelta()) # 생성된 객체 p를 통해 getDelta()함수를 호출

main()