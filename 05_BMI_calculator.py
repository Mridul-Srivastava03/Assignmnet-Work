height = float(input("Enter the height (in metre): "))
weight = float(input("Enter the weight (in kg): "))

BMI = weight/(height ** 2)

if BMI >= 30:
    print("Obesity")
elif (BMI >= 25) and (BMI < 30):
    print("Overweight")
elif (BMI >= 18.5) and (BMI < 25):
    print("Normal")
else:
    print("Underweight")
