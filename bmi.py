def calculate_bmi(height, weight):
    print("Height = " + str(height))

    print("Weight = " + str(weight))

    # calculate bmi, need to get height and weight from calculate_bmi function
    bmi = (weight / (height * 2))
    print("BMI = " + str(bmi))

    if (bmi < 18.5):
        print("Underweight")
        return -1
    elif (18.5 <= bmi <= 25.0):
        print("Normal weight")
        return 0
    else:
        print("Overweight")
        return 1

calculate_bmi(height=1.73, weight=57)