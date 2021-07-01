from Problem import Numeric


def main():
    p = Numeric()
    p.setVariables()
    gradientDscent(p)
    
    p.describe()
    displaySetting(p)
    p.report()
    
def gradientDscent(p):
    currentP = p.randomInit()   # 생성된 객체 p를 통해 randomInit함수를 호출한다. # 'currentP' is a list of values
    valueC = p.evaluate(currentP) # 생성된 객체 p를 통해 evaluate함수를 호출한다.
    
    i = 0
    while i < p.getLimit():
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
    
def displaySetting(p):
    print()
    print("Search algorithm: Gradient Descent")
    print()
    print("Mutation step size:", p.getAlpha())  # 생성된 객체 p를 통해 getAlpha 함수를 호출한다.
    
main()