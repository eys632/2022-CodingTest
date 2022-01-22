"""

설명
    - n의 제곱근의 제곱이 n이려면 (n 제곱근-정수 n 제곱근)=0이어야 한것을
      이용하여 성립 시 n의 제곱근 +1의 제곱을 return 시켜주었습니다.


함수
    pow
        - import math
        - math.pow(a,b) -> a의 b 제곱
    sqrt
        - import math
        - math.sqrt(a) -> a의 제곱근

"""


# Code
def solution(n):
    import math
    if math.sqrt(n) - int(math.sqrt(n)) == 0:
        return (int(math.sqrt(n)) + 1) ** 2
    else:
        return -1
