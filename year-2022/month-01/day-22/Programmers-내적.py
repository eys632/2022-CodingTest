"""

설명
    - for문을 사용하여 원소의 개수만큼 원소들의 곱을 a리스트에 넣어주었습니다.
    - a리스트를 sum을 이용해 모두 더해주었습니다.

"""


# Code
def solution(a, b):
    for i in range(len(a)):
        a[i] = a[i]*b[i]
    return sum(a)
