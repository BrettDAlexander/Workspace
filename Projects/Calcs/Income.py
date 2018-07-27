hourly = float(input("What is your hourly wage? "))
taxpercent = float(input("What percentage of taxes are taken from your income? "))
hours = float(input("How many hours do you work in a week? "))

tax = abs(taxpercent/100-1)

if hours>40:
    overtime = (hours-40)*(hourly*1.5)
    hours = 40
else:
    overtime = 0.0

daily = hourly*12
weekly = hourly*hours+overtime
biweekly = weekly*2
monthly = weekly*4
salary = weekly*52

print("---Income Before Taxes---")
table = {'Daily':daily, 'Weekly':weekly, 'Biweekly':biweekly, 'Monthly':monthly, 'Salary':salary}
for interval, income in table.items():
    print('{0:<8} | {1:>13}'.format(interval, '${:,.2f}'.format(income)))

if taxpercent>0:
    table2 = {'Daily':daily*tax, 'Weekly':weekly*tax, 'Biweekly':biweekly*tax, 'Monthly':monthly*tax, 'Salary':salary*tax}
    print("\n---Income After Taxes---")
    for interval, income in table2.items():
        print('{0:<8} | {1:>13}'.format(interval, '${:,.2f}'.format(income)))
else:
    pass