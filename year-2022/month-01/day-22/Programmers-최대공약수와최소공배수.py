"""

설명
    - 최대공약수를 구해주는 함수인 gcd를 이용하여 최대공약수를 구해주었습니다.
    - 최소공배수는 두 수의 곱에 두수의 최대공약수를 나눠서 구해주었습니다.
    - 구해준 것들을 list형태에 바로 넣어 return 시켜주었습니다.


함수
    최대공약수
        - from math import gcd
        - gcd(숫자들) -> 숫자의 최대공약수(둘 이상의 정수의 공약수 중에서 가장 큰 것)
        - lcm(숫자들) -> 숫자의 최소공배수(둘 이상의 정수의 공배수 중에서 가장 작은 것)

"""


# Code
def solution(n, m):
    from math import gcd
    return [gcd(n, m), int(n * m / gcd(n, m))]