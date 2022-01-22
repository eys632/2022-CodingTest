"""

설명
    - s를 sorted를 사용하여 정렬해 주었습니다. sorted로 정렬하면 list로 변환되었습니다.
    - [::-1]을 사용하여 정렬한 s 문자열을 뒤집어주었습니다.
    - join을 사용하여 list에 들어가있는 s를 합쳐주었습니다.


함수
    sort()와 sorted()
        - sort() -> 본체의 리스트를 정렬해서 변환
        - sorted() -> 본체 리스트는 내버려두고, 정렬한 새로운 리스트 변환
    join
        - join 함수는 문자열을 합치는 역할을 합니다.
        - "구분자".join(리스트) -> 리스트를 구분자를 삽입

"""


# Code
def solution(s):
    return "".join(sorted(s)[::-1])
