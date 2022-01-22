"""

설명
    - 함수 solution은 정수 n을 매개변수로 입력받습니다.
    - n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴하였습니다.
    
    
함수
    map 
        - map은 리스트나 튜플의 형태에 있는 값들을 원하는 값으로 한번에 변환 시켜주는 함수입니다.
        - list(map(함수,리스트))이면 리스트에 값들을 함수에 맞게 변환하고 리스트로 저장합니다.
        - map은 정수를 변환할 수 없다.
        - list(map(int,리스트)) -> 리스트안의 값을 정수로 변환
    reverse
        - reverse = True를 사용하여 역순으로 배치합니다.
        - reverse = 역전
    join
        - join 함수는 문자열을 합치는 역할을 합니다.
        - "구분자".join(리스트) -> 리스트를 구분자를 삽입

"""


# Code
def solution(n):
    answer = list(sorted(map(int, str(n)), reverse=True))
    return int("".join(map(str, answer)))
