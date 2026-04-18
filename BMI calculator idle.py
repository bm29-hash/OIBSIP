while True:
    try:
        # Input
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        # Validation
        if weight <= 0 or height <= 0:
            print("Invalid input! Values must be greater than 0.\n")
            continue

        # Calculation
        bmi = weight / (height ** 2)

        # Output
        print("\nYour BMI is:", round(bmi, 2))

        # Category
        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

        # Run again option
        choice = input("\nDo you want to calculate again? (yes/no): ").lower()
        if choice != "yes":
            print("Thank you for using BMI Calculator!")
            break

    except ValueError:
        print("Please enter valid numbers only!\n")
