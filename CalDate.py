def year_to_days(year):
    days = (int(year) - 1) * 365
    return days

def month_to_days(month):
    days = (int(month) - 1) * 31
    return days

def date_to_days(date):
    days = (int(date))
    return days

def all_days(date):
    year = date[0:4]
    year = year_to_days(year)

    month = date[4:6]
    month = month_to_days(month)

    date = date[6:8]
    days = date_to_days(date)

    sum = year + month + days
    return sum
    
def days_calculation(days1,days2):
    if days1 < days2:
        result = days2 - days1
        return result
    else:
        result = days1 - days2
        return result

#入力は文字型
date1 = input("最初の日付をyyyymmddで入力してください")
date2 = input("後の日付をyyyymmddで入力してください")

#すべてを日数に直したもの
days1 = all_days(date1)
days2 = all_days(date2)

result = days_calculation(days1,days2)
print("その期間は"+str(result)+"日です")