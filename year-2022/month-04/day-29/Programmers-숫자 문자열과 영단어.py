"""
설명
    - 변경 전 문자열과 변경 후 문자열을 리스트로 만들어 놓았습니다.
    - replace 함수를 사용하여 문자열의 특정 문자를 원하는 문자열로 바꾸어 주었습니다.
"""


# Code
def solution(s):
    number = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    num = ["0","1","2","3","4","5","6","7","8","9"]

    for i in range(len(number)):
        if number[i] in s:
            s = s.replace(number[i],num[i])
    return int(s)