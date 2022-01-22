"""

설명
    - 문자열을 원하는 개수만큼 변수에 넣으려면 (문자*횟수)
    - list[-4:] : list에 뒤에서 4번째 ~ 1번째 까지


함수
    list[:]
        - :은 처음과 끝을 의미할 때 사용합니다.

"""


# Code
def solution(phone_number):
    answer = '*' * (len(phone_number) - 4)
    answer += phone_number[-4:]
    return answer
