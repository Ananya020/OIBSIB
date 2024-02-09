def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive numbers.")
        return

    bmi = calculate_bmi(weight, height)

    category = classify_bmi(bmi)
    
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
