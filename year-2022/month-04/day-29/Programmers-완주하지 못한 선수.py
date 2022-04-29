"""
설명
    - 각 이름의 Hash 값을 구하고, 이 값들의 합을 구해주었습니다.
    - sumHash에서 완주한 선수의 Hash 값을 빼주었습니다.
    - sumHash에서 완주자들을 제외시키면, 한 명만 남게 될 것이고 그 사람이 정답입니다.
"""


# Code
def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)

    for comp in completion:
        sumHash -= hash(comp)

    return hashDict[sumHash]