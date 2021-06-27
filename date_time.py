import datetime as datetime

today = datetime.datetime.now()
today_short = today.strftime("%d/%m/%Y(%H:%M)")
thirty_days_later = today + datetime.timedelta(days=30)
thirty_days_later_short = thirty_days_later.strftime("%d/%m/%Y")


print(today_short)
print(thirty_days_later_short)
