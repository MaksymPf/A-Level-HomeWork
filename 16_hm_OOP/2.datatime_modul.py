import datetime

now = datetime.date.today()
holidays = {datetime.date(now.year, 8, 24)} # you can add more here
businessdays = 0 

for i in range(1, 32):
    thisdate = datetime.date(now.year, now.month, i)

    if thisdate == now:
        break
    elif thisdate.weekday() < 5 and thisdate not in holidays: # Monday == 0, Sunday == 6 
        businessdays += 1

print (businessdays)

input()