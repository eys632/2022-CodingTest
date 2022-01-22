"""

설명
    - if문을 사용하여 num을 2로 나눴을 때의 나머지가 0이면 짝수로 하여 return 시켜주었습니다.
    - 홀수는 반대의 상황이니 else를 사용하여 return 시켜주었습니다.

"""


# Code
def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
