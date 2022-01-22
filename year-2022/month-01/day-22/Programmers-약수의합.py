"""

설명
    - n 값을 1부터 n+1 번 i값으로 나눠주었을 때 나머지가 0인 값들은 n의 약수가 된다.
    - answer을 0으로 지정해 놓고 n의 약수인 i값을 answer에 더해준다.
    - answer에는 n의 약수의 합들이 들어가 있고 그 값을 return 시켜주었다.

"""


# Code
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
    return answer
