"""
以下の二つの事実を利用して、任意の日付の曜日を求める。
１．月曜日の次は必ず火曜日になり、その次は必ず水曜日になる。
２．2000年の1月1日が土曜日である。
"""

def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapmonth = []
    
# 2000年1月1日の何日後かをもとめる
def days(year, month, day):
    res = 0
    diffyear = year - 2000
    diffmonth = month - 1
    diffday = day - 1
    assert diffyear >= 0
    
    return diffyear * 365 + diffmonth * 30 + diffday
    

if __name__ == "__main__":
    print(isleap(2024))
    print(isleap(1900))
    print(isleap(2000))
    
    print(days(2000, 1, 3))