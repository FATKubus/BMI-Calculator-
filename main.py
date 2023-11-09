
def calculator_bmi():
    weight = float(input("Enter your weight in kilograms:"))
    height = float(input("Enter your height in meters:"))
    bmi = weight / (height * height)
    if bmi < 18.5:
        print("Underweight")
    if 18.5 <= bmi < 25:
        print("Normal weight")
    if 25 <= bmi < 30:
        print("Overweight")
    if 30 <= bmi < 35:
        print("1st degree overweight")
    if 35 <= bmi < 40:
        print("2nd degree overweight")
    if bmi > 40:
        print("Extreme obesity")

    print(f"Your BMI is: {bmi}")

calculator_bmi()