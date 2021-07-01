from Problem import *
from Optimizer import *

def main():
    p, pType = selectProblem()
    alg = selectAlgorithm(pType)
    alg.run(p)
    p.describe()
    alg.displaySetting()
    p.report()
    
def selectProblem():
    print('Select the problem type:')
    print('   1. Numerical Optimization')
    print('   2. TSP')
    pType = int(input('Enter the number:'))
    if pType == 1:        # 입력받은 problem타입이 Numeric일 경우 Numeric형 객체 생성
        p = Numeric()
    elif pType == 2:     # 입력받은 problem타입이 Tsp일 경우 Tsp형 객체 생성
        p = Tsp()
    p.setVariables()     # setVariables 함수를 통해 변수들을 초기화 한다.
    return p, pType

def selectAlgorithm(pType):
    print()
    print('Select the search algorithm:')
    print('  1. Steepest-Ascent')
    print('  2. First-Choice')
    print('  3. Gradient Descent')
    
    optimizers = {1: 'SteepestAscent()', 
                  2: 'FirstChoice()', 
                  3: 'GradientDescent()'}      #dict형으로 optimizers를 선언한다.
    
    while True:
        aType = int(input('Enter the number:'))  # input 명령어를 통해 실행하기 위한 알고리즘을 입력받는다.
        if not invalid(pType, aType):
            break
    
    alg = eval(optimizers[aType])        # eval(optimizers[aType])를 통해 알고리즘에 해당하는 객체를 생성한다.
    alg.setVariables(aType,pType)        # setVariable(aType,pType)을 통해 생성된 객체에 aType과 pType을 할당하는 함수를 호출한다.
    
    return alg

def invalid(pType, aType):
    if pType == 2 and aType == 3:   # pType이 Tsp이고, algorithm이 Gradient Descent일때
        print('You cannot choose Gradient Descent with TSP')
        return True
    else:
        return False
main()