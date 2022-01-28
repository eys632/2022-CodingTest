"""

설명
    - 문자열 n에 1부터 한번씩 나눠서 나머지가 1인지 확인을 해봤습니다.
      그러고 1이 아니면 나눠주는 수에 1을 더해 반복문을 실행 시켜주었습니다.

"""


# Code
def solution(n):
    i = 1
    while True:
        if n % i == 1:
            return i
            break
        i += 1


print(solution(12))
