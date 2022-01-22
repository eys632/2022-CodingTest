"""

설명
    - date에 원하는 년,월,일을 입력한 후에(.weekday)를 해주면 제가 입력한
      date의 요일을 월,화,수... 순서대로 0,1,2... 으로 바꿔주었습니다.
    - 월요일~일요일까지 들어있는 리스트를 인덱싱하여 return 시켜주었습니다.


함수
    date
        - date(year,month,day) -> year-month-day 형식으로 받아드림
    weekday
        - date.weekday() -> date의 년-월-일에 따른 요일을 숫자로 리턴

"""


# Code
def solution(a, b):
    from datetime import date
    return ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"][date(2016, a, b).weekday()]
