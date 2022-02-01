"""

설명
    - commands의 길이만큼 for문을 반복시켜주었고 commands에 처음부터 끝까지 빼오고 그걸 정렬한것에서 commands에 3번째 꺼를 사용해서 특정자리에 있는 원소를 commands 리스트에 넣어주었다
    - 새로 리스트를 만들기 싫어서 그렇게 해봤다.

"""


# Code-1
def solution(array, commands):
    for i in commands:
        print(sorted(array[i[0] - 1:i[1]])[i[2] - 1])


# Code-2
def solution(array, commands):
    for i in range(len(commands)):
        commands[i] = sorted(array[commands[i][0] - 1:commands[i][1]])[commands[i][2] - 1]
    return commands
