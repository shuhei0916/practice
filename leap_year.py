"""
以下の二つの事実を利用して、任意の日付の曜日を求める。
１．月曜日の次は必ず火曜日になり、その次は必ず水曜日になる。
２．2000年の1月1日が土曜日である。
"""

import datetime

def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
leapmonth = []
    
# 2000年1月1日の何日後かをもとめる
def days(year, month, day):
    res = 0

    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isleap(year):
        days_of_month[1] = 29

    for y in range(2000, year):
        # print(y, end=": ")
        if isleap(y):
            res += 366
            # print(isleap(y), res)

        else:
            res += 365
            # print(isleap(y), res)

    # print("=====")
    for m in range(1, month):
        res += days_of_month[m - 1]
        # print(m, ": ", res)

    # print("=====")
    for d in range(1, day):
        res += 1
        # print(d, ": ", res)

        

    # diffyear = year - 2000
    # diffmonth = month - 1
    # diffday = day - 1
    # assert diffyear >= 0
    
    return res
    

if __name__ == "__main__":
    # print(isleap(2024))
    # print(isleap(1900))
    # print(isleap(2000))
    
    # print(days(2000, 1, 3))
    # print(days(2000, 2, 1))
    # print(days(2000, 3, 1))

    # print(days(2002, 12, 5))

    dt1 = datetime.datetime(2000, 1, 1)


    week = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]


    dt3 = datetime.datetime(2024, 3, 18)
    print(days(2024, 3, 18))


    print(days(2024, 3, 18))
    print(week[days(2024, 3, 18) % 7])
