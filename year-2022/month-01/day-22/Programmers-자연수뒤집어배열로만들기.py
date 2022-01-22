"""

설명
    - for a in str(n)은 n=123인 경우 n을 문자열로 만듦으로써 한줄에 숫자 하나씩 a에 순서대로 넣어주었다.
    - for문의 첫번째 a는 1, 두번째 a는 2, 세번째 a는 3이고 [int(a) for a in str(n)]는 리스트 안에 a를 정수형으로 바꿔서 넣어주었다.
    - 완성시킨 리스트를 뒤집기위해 [::-1]을 사용하였다.


함수
    array[::] 용법
        - array[a:b:c] -> index a부터 index b 까지 c의 간격으로 배열을 만들어준다.
            - a = None -> 처음부터
            - b = None -> 할 수 있는 데까지 (c가 양수라면 마지막 index까지, c가 음수라면 첫 index까지입니다.)
            - c = None -> 한 칸 간격으로

"""


# Code
def solution(n):
    return [int(a) for a in str(n)][::-1]
