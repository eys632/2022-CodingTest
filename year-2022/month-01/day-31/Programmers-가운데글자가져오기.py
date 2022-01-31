"""

설명
    - 짝수문자열은 문자열 개수를 2로 나눈거에 1을 뺴준것과 그냥 2로 나눠준거를 출력
    - 홀수문자열은 2로 나눠준것만 출력

"""


# Code
def solution(s):
    if len(s) % 2 == 0:
        return s[int(len(s) / 2) - 1] + s[int(len(s) / 2)]
    else:
        return s[int(len(s) / 2)]
