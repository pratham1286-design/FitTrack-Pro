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
        return bmr
    def TDEE():
        bmr_value=bmr()
        print("\nSelect Activity Level")
        print("1. Sedentary")
        print("2. Lightly Active")
        print("3. Moderately Active")
        print("4. Very Active")
        print("5. Extra Active")
        choice = int(input("Enter choice: "))
        if choice == 1:
            activity = 1.2
        elif choice == 2:
            activity = 1.375
        elif choice == 3:
            activity = 1.55
        elif choice == 4:
            activity = 1.725
        elif choice == 5:
            activity = 1.9
        else:
            print("Invalid Choice")
            return
        tdee = bmr_value * activity
        print(f"\nYour TDEE is : {tdee:.2f} kcal/day")
        return tdee
    def DailyCalreq():
        tdee=TDEE()
        import csv
        with open("userinfo.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                goal = row["Fitness_Goal"]
        if goal == "Lose Fat":
            calories = tdee - 500
        elif goal == "Muscle Building":
            calories = tdee + 300
        else:
            calories = tdee
        print(f"\nDaily Calories Required : {calories:.2f} kcal/day")
    def dailymacros():
        calories = DailyCalreq()
        with open("userinfo.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                weight = float(row["Weight"])
        protein = weight * 2
        fat = (calories * 0.25) / 9
        carbs = (calories - (protein * 4 + fat * 9)) / 4
        print(f"\nProtein : {protein:.2f} g")
        print(f"Carbs   : {carbs:.2f} g")
        print(f"Fats    : {fat:.2f} g")
    def waterintake():
        with open("userinfo.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                weight = float(row["Weight"])
        water = weight * 35
        print(f"\nDaily Water Intake : {water/1000:.2f} Litres")
    def idealweight():
        with open("data/userinfo.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                gender = row["Gender"].lower()
                height = float(row["Height"])
            inches = height / 2.54
        if gender == "male":
            ideal = 50 + 2.3 * (inches - 60)
        else:
            ideal = 45.5 + 2.3 * (inches - 60)
        print(f"\nIdeal Weight : {ideal:.2f} kg")
    while True:
        print("======Fitness Tools======")
        print("1 - BMI")
        print("2 - BMR")
        print("3 - TDEE")
        print("4 - Calculate Daily Calories requirement")
        print("5 - Calculate Daily Macros")
        print("6 - Total Water Intake")
        print("7 - Calculate Your Ideal Weight")
        print("8 - Exit")
        tools=int(input("Select the option(1,2,3,4,5,6,7,8): "))
        if tools==1:
            bmi()
        elif tools==2:
            bmr()
        elif tools==4:
            DailyCalreq()
        elif tools==3:
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
