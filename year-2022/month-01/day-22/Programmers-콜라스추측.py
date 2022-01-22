"""

Code-1 설명
    - while문을 사용하여 num이 1이 될 때 까지 반복시켰습니다.
    - if문과 else문을 이용하여 짝수일 때와 홀수일 때를 나눠주었습니다.
    - 반복 횟수가 500이 넘으면 answer = -1이고 while문을 멈춰주었습니다.

Code-2 설명
    - "수행문장 if 조건문 else 조건문" 이렇게도 사용할 수 있습니다.
    - for문을 사용하여 500번을 반복시키고 짝수일 때와 홀수일 때를 if문과 else문으로 한줄에 적어주었습니다.
    - 만약 num이 1이면 i+1울 return 시키는데 그 이유는 i변수는 0부터 시작해서 반복문이 한번 끝날때마다 i+=1이 되기 때문입니다.
함수
    "수행문장 if 조건문 else 조건문"
        - if 조건문을 만족시키면 수행문장을 실행시키고 그렇지 않다면 else 조건문을 실행시킨다.

"""


# Code-1
def solution(num):
    answer = 0

    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        answer += 1
        if answer >= 500:
            answer = -1
            break
    return answer


# Code-2
def solution(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        if num == 1:
            return i + 1
    return -1
