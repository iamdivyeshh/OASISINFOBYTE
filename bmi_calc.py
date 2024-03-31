name = input("Enter Your Name : ")
weight = float(input("Enter your weight : "))
height = float(input("Enter your height : "))

bmi = weight / (height * height)
if bmi < 18.5:
    print (f"{name} is Underweight by {bmi} BMI")
elif bmi <= 24.9:
    print(f"{name} is Normal weight by {bmi} BMI")
elif bmi <= 29.9:
    print(f"{name} is Overweight by {bmi} BMI")
else:
    print(f"{name} is Obese by {bmi} BMI")
