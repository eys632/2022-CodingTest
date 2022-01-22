"""

설명
    - numpy의 행렬의 합을 사용하였습니다.
    - ndarray 형태로 answer에 저장이 되어 tolist를 사용하여 list로 변환했습니다.

"""


# Code-1
def solution(arr1, arr2):
    import numpy as np
    answer = np.array(arr1) + np.array(arr2)
    return answer.tolist()


# Code-2
def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1
