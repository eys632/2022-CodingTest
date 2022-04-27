"""
설명
    - arrr 값을 하나씩 꺼내 원하는 값을 찾아주었습니다.
"""


# Code
def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
        return answer
    else:
        return sorted(answer)