"""
설명
    - 앞의 값이랑 위의 값이 같지 않은 것만 answer 리스트에 추가해주었습니다.
    - 그렇게 하면 가장 마지막의 값은 가져올 수 없게 되어 따로 추가해주었습니다.
"""


# Code
def solution(arr):
    answer = []

    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
    answer.append(arr[-1])
    return answer
