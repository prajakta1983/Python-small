# BMI Calculator
height=float(input("Enter your height (In m:"))
weight=float(input("Enter your weight (In kg:"))
bmi= weight / ((height)*(height))
print("Your BMI is: " , bmi)
if(bmi<18.5):
    print("You are underweight")
    print("You need to increase weight by " + str(18.5-bmi) + " to be in normal range")
elif(18.5<bmi<24.9):
    print("You are normal")
elif(25<bmi<29.9):
    print("You are overweight")
    print("You need to reduce weight by " + str(bmi-24.9) + " to be in normal range")
elif(bmi>30):
    print("You are obese")
    print("You need to increase weight by " + str(bmi-24.9) + " to be in normal range")
