def solution(arr):

    for i in range(len(arr)):
        try:
            if arr[i] == arr[i+1]:
                del arr[i+1]
            elif arr[i] != arr[i+1]:
                pass
        except IndexError:
            print(arr)



print(solution([4,4,4,3,3]))