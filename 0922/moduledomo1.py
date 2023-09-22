#알고 있으면 좋은 모듈
from datetime import datetime

import calendar #파이썬의 캘린더는 첫째 날이 월요일이다.
import random

print(calendar.month(2023, 9))
print(calendar.calendar(1)) #전체 달 출력
print(datetime.now())
print(random.randint(0,99)) #(랜덤 범위를 지점해준다.)

num1 = random.randint(0,999)
num1 = str(num1).zfill(000)
print(num1)
