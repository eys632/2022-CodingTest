# def solution(strings, n):
#     d = dict()
#     for i in strings:
#         d[i[n]] = i
#         print(i)
#     print(d)
#     for i in range(len(strings)):
#         print(sorted(d.items())[i][1])
#         strings[i] = sorted(d.items())[i][1]
#
#     return strings


print(solution(["abce", "abcd", "cdx"], 2))
