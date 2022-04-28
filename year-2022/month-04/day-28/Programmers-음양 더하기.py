"""
설명
    - signs의 값을 각각 확인하여 False이면 그때의 인덱스 위치의 값을 -를 붙여주었습니다.
    - 변화시킨 absolutes를 마지막에 sum을 이용해 모두 더해주었습니다.
"""

def solution(absolutes, signs):
    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)