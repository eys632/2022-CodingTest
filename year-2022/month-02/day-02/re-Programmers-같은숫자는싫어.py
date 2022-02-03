# def solution(arr):
#     try:
#         for i in range(len(arr)):
#             if arr[i] == arr[i + 1]:
#                 del arr[i + 1]
#             elif arr[i] != arr[i + 1]:
#                 pass
#     except IndexError:
#         return arr

# def solution(arr):
#     i = 0
#     j = 1
#     while True:
#         while arr[i] == arr[j]:
#             del arr[j]
#             j = +1
#         print(arr,i,j)
#         j=1
#         i=+1
#     return arr

# key 써서 해봐


print(solution([4, 4, 4, 3, 3]))
print(solution([1, 1, 3, 3, 0, 1, 1]))
