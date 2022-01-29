"""

설명
    - 0~9까지 반복문을 돌려 i에 넣어주었고 numbers 리스트에 i가 있는지 not in 을 사용하여 알아보았다.

"""


# Code
def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer
