# BMI Calculator
height=float(input("Enter your height (In m:"))
weight=float(input("Enter your weight (In kg:"))
bmi= weight / ((height)*(height))
print("Your BMI is: " , bmi)
if(bmi<18.5):
    print("You are underweight")
elif(18.5<bmi<24.9):
    print("You are normal")
elif(25<bmi<29.9):
    print("You are overweight")
elif(bmi>30):
    print("You are obese")
