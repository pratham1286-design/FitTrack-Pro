def analytics():
    from datetime import date
    today=date.today()
    import csv
    def usersum():
        with open("userinfo.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                name=row[1]
                age=row[2]
                height_cm=row[4]
                curweight=row[5]
                Fitnessgoal=row[7]
                height_m=float(height_cm/100)
                bmi=curweight/(height_m**2)
                if bmi<18.5:
                    print("UnderWeight")
                    condition="UnderWeight"
                elif bmi<25:
                    print("Normal Weight")
                    condition="Normal Weight"
                elif bmi<30:
                    print("Overweight")
                    condition="Overweight"
                else:
                    print("Obese")
                    condition="Obese"
                gender=(row[3])
                if gender=="Male":
                    bmr = (10 * curweight) + (6.25 * height_cm) - (5 * age) + 5
                    them="his"
                    otherthem="him"
                else:
                    bmr = (10 * curweight) + (6.25 * height_cm) - (5 * age) - 161
                    them="her"
                    otherthem="her"
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
                tdee = bmr * activity
                print(f"Name : {name} of {age}years age with height:{height_cm}cm and weight:{curweight}kgs has a BMI of {bmi} making {otherthem} - {condition} and {them} BMR is {bmr} and {them} TDEE based on {them} activity level is {tdee} ")
                return name,Fitnessgoal
    def nutrisum():
        with open("nutrition.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            calsconsumed=0
            proconsumed=0
            carbsconsumed=0
            fatconsumed=0
            for row in reader:
                if row[0]==today:
                    calsconsumed+=row[6]
                    proconsumed+=row[7]
                    carbsconsumed+=row[8]
                    fatconsumed+=row[9]
                    nameofstudent=usersum()
                print(f"Name : {nameofstudent}, today's consumed calories = {calsconsumed} kcal , today's consumed protein = {proconsumed},today's consumed carbs = {carbsconsumed},today's consumed fats = {fatconsumed}.")
    def worksum():
        total_workouts = 0
        total_duration = 0
        total_burned = 0
        try:
            with open("workouts.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    total_workouts += 1
                    total_duration += float(row["Duration(mins)"])
                    total_burned += float(row["Calories(kcal)"])
        except FileNotFoundError:
            print("No workout data found yet.")
            return
        if total_workouts == 0:
            print("workouts.csv is empty.")
            return
        print(f"\n--- Workout Summary ---")
        print(f"Total Workouts      : {total_workouts}")
        print(f"Total Duration      : {total_duration:.0f} min")
        print(f"Total Cal Burned    : {total_burned:.0f} kcal")
        print(f"Avg Duration/Workout: {total_duration / total_workouts:.1f} min")
    while True:
        print("="*10,"Analytics Dashboard","="*10)
        print("1 - User Summary")
        print("2 - Nutrition Analytics")
        print("3 - Workout Analytics")
        print("4 - Back")
        ana=int(input("Choose the function(1,2,3,4): "))
        if ana==1:
            usersum()
        elif ana==2:
            nutrisum()
        elif ana==3:
            worksum()
        elif ana==4:
            break
        else:
            print("Invalid Input")