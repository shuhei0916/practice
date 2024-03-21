"""
以下の二つの事実を利用して、任意の日付の曜日を求める。
１．月曜日の次は必ず火曜日になり、その次は必ず水曜日になる。
２．2000年の1月1日が土曜日である。
"""

import datetime

def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
leapmonth = []
    
# 2000年1月1日からの経過日数を計算する
def days(year, month, day):
    res = 0

    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isleap(year):
        days_of_month[1] = 29

    for y in range(2000, year):
        if isleap(y):
            res += 366
        else:
            res += 365

    for m in range(1, month):
        res += days_of_month[m - 1]

    for d in range(1, day):
        res += 1
    
    return res
    
def get_weekday(year: int, month: int, day: int) -> str:
    week = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]
    
    index = days(year, month, day) % 7
    return week[index]
    

if __name__ == "__main__":
    print(get_weekday(2024, 3, 21))