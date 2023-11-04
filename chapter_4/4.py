# 2
import calendar
# 3
help(calendar)
# 4
leap = calendar.isleap(2027)
# 5
days = ["понедельник", "вторник", "среда",
        "четверг", "пятница", "суббота", "воскресенье"]
day_of_week = days[calendar.weekday(1995, 6, 25)]
# 6
cal = calendar.TextCalendar(calendar.MONDAY)
for i in range(1, 13):
        print(cal.formatmonth(2023, i))