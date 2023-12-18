import datetime
birthYear=int(input("Enter your birth-year"))
print(birthYear)
currentDate=datetime.date.today()
currentYear=currentDate.year
print(currentYear)
print("Your age is " + str(currentYear-birthYear))

