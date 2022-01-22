"""

Code-1 설명
    - 2중 for문을 사용하여 행과 열을 나타내어주었습니다.
    - end를 사용해 밑에줄에 출력하는 것을 막았습니다.

함수
    strip()
        - 문자열.strip() -> 공백 제거
        - abc.strip("a") -> a제거
        - abab.lstrip("a") -> 선행문자 a만 지움
        - abab.rstrip("b") -> 후행문자 b만 지움

Code-2 설명
    - *을 a번 만큼 찍고 줄을 넘긴후 이것을 b번 반복했습니다.


"""

# Code-1
a, b = map(int, input().strip().split(' '))
for i in range(b):
    for i in range(a):
        print("*", end="")
    print()


# Code-2
a, b = map(int, input().strip().split(' '))
print(('*' * a + '\n') * b)
