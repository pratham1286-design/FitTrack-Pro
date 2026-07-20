def Tools():
    import csv
    def bmi():
        while True:
            print("choose the option: ")
            print("1 - Your BMI")
            print("2 - Calculate other BMI")
            print("3 - Go Back")
            bm=int(input("Choose the function you want to use(1,2,3): "))
            if bm==1:
                with open("userinfo.csv","r") as file:
                    reader=csv.DictReader(file)
                    for row in reader:
                        height_cm=float(row["Height"])
                        weight=float(row["Weight"])
                    height_m=float(height_cm/100)
                    bmi=weight/(height_m**2)
                    print("Your BMI: ",bmi)
                    if bmi<18.5:
                        print("UnderWeight")
                    elif bmi<25:
                        print("Normal Weight")
                    elif bmi<30:
                        print("Overweight")
                    else:
                        print("Obese")
            elif bm==2:
                    weight=float(input("Input Weight in kgs: "))
                    height=float(input("Input Height in metres: "))
                    bmi=weight/(height**2)
                    print("Your BMI: ",bmi)
                    if bmi<18.5:
                        print("UnderWeight")
                    elif bmi<25:
                        print("Normal Weight")
                    elif bmi<30:
                        print("Overweight")
                    else:
                        print("Obese")
            elif bm==3:
                break
            else:
                print("Invalid Input")
    def bmr():
        while True:
            print("choose the option: ")
            print("1 - Your BMR")
            print("2 - Calculate other BMR")
            print("3 - Go Back")
            br=int(input("Choose the function you want to use(1,2,3): "))
            if br==1:
                with open("userinfo.csv","r") as file:
                    reader=csv.DictReader(file)
                    for row in reader:
                        height_cm=float(row["Height"])
                        weight=float(row["Weight"])
                        age=int(row["Age"])
                        gender=(row["Gender"])
                        if gender=="Male":
                            bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) + 5
                        elif gender=="Female":
                            bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) - 161
                        else:
                            print("Invalid Gender")
                            return
                    print(f"Your BMR is: {bmr:.2f} kcal/day")
            elif br==2:
                weight = float(input("Enter your weight (kg): "))
                height = float(input("Enter your height (cm): "))
                age = int(input("Enter your age: "))
                gender = input("Enter your gender (M/F): ").upper()
                if gender == "M":
                    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
                elif gender == "F":
                    bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
                else:
                    print("Invalid gender.")
                    return
                print(f"Your BMR is: {bmr:.2f} kcal/day")
    def DailyCalreq():
        pass
    def TDEE():
        pass
    def dailymacros():
        pass
    def waterintake():
        pass
    def idealweight():
        pass
    while True:
        print("======Fitness Tools======")
        print("1 - BMI")
        print("2 - BMR")
        print("3 - Calculate Daily Calories requirement")
        print("4 - TDEE")
        print("5 - Calculate Daily Macros")
        print("6 - Total Water Intake")
        print("7 - Calculate Your Ideal Weight")
        print("8 - Exit")
        tools=int(input("Select the option(1,2,3,4,5,6,7,8): "))
        if tools==1:
            bmi()
        elif tools==2:
            bmr()
        elif tools==3:
            DailyCalreq()
        elif tools==4:
            TDEE()
        elif tools==5:
            dailymacros()
        elif tools==6:
            waterintake()
        elif tools==7:
            idealweight()
        elif tools==8:
            break
        else:
            print("Invalid Input")
