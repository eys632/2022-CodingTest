"""
설명
    - seoul 리스트 안에 Kim이라는 글씨의 인덱스 위치를 찾아 출력했습니다.
"""


# Code
def solution(seoul):
    answer = seoul.index("Kim")
    return "김서방은 " + str(answer) + "에 있다"