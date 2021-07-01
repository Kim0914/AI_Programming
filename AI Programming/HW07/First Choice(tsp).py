from Problem import Tsp


def main():
    p = Tsp()
    p.setVariables()
    firstChoice(p)
    p.describe()
    displaySetting(p)
    p.report()
    
def firstChoice(p):
    current = p.randomInit()        #생성된 객체 p를 통하여 randomInit 함수를 호출한다. # 'current' is a list of values
    valueC = p.evaluate(current)      #생성된 객체 p를 통하여 evalutae 함수를 호출한다.
    i = 0
    while i < p.getLimit():        #생성된 객체 p를 통하여 getLimit 함수를 호출한다.
        successor = p.randomMutant(current) #생성된 객체 p를 통하여 randomMutant 함수를 호출한다.
        valueS = p.evaluate(successor)      #생성된 객체 p를 통하여 evaluate 함수를 호출한다.
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    p.setSolution(current)   # 생성된 객체 p를 통해 setSolution 함수를 호출한다.
    p.setMinimum(valueC)     # 생성된 객체 p를 통해 setMinimum 함수를 호출한다.
    
def displaySetting(p):
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()

main()
    