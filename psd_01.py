"""
#-- 날짜 입력 함수

from datetime import datetime

today = datetime.now()
print(today)
print()
print("입력 날짜:{0!s}".format(today.strftime('%Y%m%d')))
print()
print("오늘 날짜:{0!s}".format(today.strftime('%x')))
print()
print("현재 시각:{0!s}".format(today.strftime('%X')))

"""
