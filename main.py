def calculate_bmi(weight, height):
    """Calculates the body mass index (BMI) for a given weight and height.

    Args:
      weight: The weight in kilograms.
      height: The height in meters.

    Returns:
      The BMI.
    """

    bmi = weight / (height ** 2)
    return bmi


def main():
    """Prompts the user for their weight and height and calculates their BMI."""

    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)

    print("Your BMI is:", bmi)

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi >= 18.5 and bmi < 25:
        print("You are a normal weight.")
    elif bmi >= 25 and bmi < 30:
        print("You are overweight.")
    elif bmi >= 30:
        print("You are obese.")


if __name__ == "__main__":
    main()
