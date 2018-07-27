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
print("Daily: ${:0,.2f}".format(daily))
print("Weekly: ${:0,.2f}".format(weekly))
print("Biweekly: ${:0,.2f}".format(biweekly))
print("Monthly: ${:0,.2f}".format(monthly))
print("Salary: ${:0,.2f}".format(salary))

if taxpercent>0:
    print("---Income After Taxes---")
    print("Daily: ${:0,.2f}".format(daily*tax))
    print("Weekly: ${:0,.2f}".format(weekly*tax))
    print("Biweekly: ${:0,.2f}".format(biweekly*tax))
    print("Monthly: ${:0,.2f}".format(monthly*tax))
    print("Salary: ${:0,.2f}".format(salary*tax))
else:
    pass