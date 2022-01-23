def solution(n):
    answer = []
    for i in range(n):
        answer.append("수") if (i % 2 == 0) else (answer.append("박"))
    return "".join(answer)
n=4

print(solution(n))
