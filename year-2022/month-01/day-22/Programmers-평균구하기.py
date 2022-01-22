"""

설명
    - 리스트안의 원소의 개수만큼 for 문을 돌려 변수 a에 원소들을 모두 더해주었습니다.
    - 모두 더한 후 원소의 개수만큼 나눠주어 평균을 구했습니다.

"""


# Code
def solution(arr):
    a = 0
    for i in range(len(arr)):
        a += arr[i]
    return a/len(arr)
