"""

설명
    - arr리스트에 최소값을 찾는 min을 사용하였습니다.
    - 찾은 최소값을 remove를 사용하여 arr리스트에서 제거해주었습니다.


함수
    list 처리
        - 리스트.append(추가할것) -> 리스트에 ()안의 값 추가
        - 리스트.insert(입력할index, 값) -> 리스트의 입력할index에 값 추가
        - 리스트1.extend(리스트2) -> 리스트1에 리스트2의 원소들을 추가
        - del 리스트[index] -> 리스트의 index 자리에 있는 값 삭제
        - 리스트.remove(값) -> 리스트안의 값 이름을 이용하여 삭제

"""


# Code
def solution(arr):
    arr.remove(min(arr))
    return arr
