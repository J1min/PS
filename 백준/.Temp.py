month_days = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31,
}
summary = 0
month, days = map(int, input().split())
for i in range(1, month):
    summary += month_days[i]
print(["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"][(summary + days)%7])