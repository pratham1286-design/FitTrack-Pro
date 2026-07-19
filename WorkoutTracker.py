def workouttracker():
    from  datetime import date
    today=date.today()
    def beginnertemplate():
        beginner_exercise=[[today,"beginner","Lat Pulldown",3,12,15,10,30],[today,"beginner","Bicep Curls",3,12,5,10,20],[today,"beginner","Tricep Bar Pushdown",3,12,15,10,20],[today,"beginner","Pushups",3,12,0,10,35],[today,"beginner","Squats",3,12,0,10,25]]
        while True:
            print("Choose the Week day:")
            print("1 - Day1")
            print("2 - Day2")
            print("3 - Day3")
            print("4 - Day4")
            print("5 - Day5")
            print("6 - Exit")
            day=int(input("Choose the day(1,2,3,4,5,6):"))
            if day in  [1,2,3,4,5]:
                import csv
                with open("workouts.csv","a",newline="") as file:
                    writer=csv.writer(file)
                    writer.writerows(beginner_exercise)
                    for exercise in beginner_exercise:
                        date,level,name,sets,reps,weight,duration,calories=exercise
                        print(f"{date} : {level} - {name} : {sets}sets*{reps}reps of {weight}, {duration}mins burning {calories}kcal")
            elif day==6:
                break
            else:
                print("Invalid Input")
    def mediumtemplate():
        mediumday1=[[today,"medium","Wide Grip Lat pulldown",3,12,32.5,10,40],[today,"medium","Chest Supported T bar row",3,12,15,10,35],[today,"medium","V Grip Lat Pulldown",3,12,25,10,30],[today,"medium","Seated Cable Row",3,12,15,10,30],[today,"medium","Single Arm Dumbbell Row",3,12,7.5,10,35]]
        mediumday2=[[today,"medium","Bicep Curls",3,12,10,10,30],[today,"medium","EZ Bar Preacher Curls",3,12,5,10,30],[today,"medium","Incline Dumbbell Curls",3,12,5,10,30],[today,"medium","Hammer Curls",3,12,5,10,30]]
        mediumday3=[[today,"medium","Wide Grip Lat pulldown",3,12,32.5,10,40],[today,"medium","Chest Supported T bar row",3,12,15,10,35],[today,"medium","V Grip Lat Pulldown",3,12,25,10,30],[today,"medium","Seated Cable Row",3,12,15,10,30],[today,"medium","Single Arm Dumbbell Row",3,12,7.5,10,35]]
        mediumday4=[[today,"medium","Bicep Curls",3,12,10,10,30],[today,"medium","EZ Bar Preacher Curls",3,12,5,10,30],[today,"medium","Incline Dumbbell Curls",3,12,5,10,30],[today,"medium","Hammer Curls",3,12,5,10,30]]
        mediumday5=[[today,"medium","Wide Grip Lat pulldown",3,12,32.5,10,40],[today,"medium","Chest Supported T bar row",3,12,15,10,35],[today,"medium","V Grip Lat Pulldown",3,12,25,10,30],[today,"medium","Seated Cable Row",3,12,15,10,30],[today,"medium","Single Arm Dumbbell Row",3,12,7.5,10,35]]
        mediumday6=[[today,"medium","Wide Grip Lat pulldown",3,12,32.5,10,40],[today,"medium","Chest Supported T bar row",3,12,15,10,35],[today,"medium","V Grip Lat Pulldown",3,12,25,10,30],[today,"medium","Seated Cable Row",3,12,15,10,30],[today,"medium","Single Arm Dumbbell Row",3,12,7.5,10,35]]
        while True:
            print("Choose the day of the MEDIUM WORKOUT: ")
            print("1 - Day1 [BACK DAY]")
            print("2 - Day2 [BICEP DAY]")
            print("3 - Day3 [CHEST DAY]")
            print("4 - Day4 [TRICEP DAY]")
            print("5 - Day5 [SHOULDER DAY]")
            print("6 - Day6 [LEG DAY]")
            print("7 - EXIT")
            day=int(input("Choose the Day(1,2,3,4,5,6,7): "))
            if day==1:
                import csv
                with open("workouts.csv","a",newline="") as file:
                    writer=csv.writer(file)
                    writer.writerows(mediumday1)
                    for exercise in mediumday1:
                        date,level,name,sets,reps,weight,duration,calories=exercise
                        print(f"{date} : {level} - {name} : {sets}sets*{reps}reps of {weight}, {duration}mins burning {calories}kcal")
            elif day==2:
                import csv
                with open("workouts.csv","a",newline="") as file:
                    writer=csv.writer(file)
                    writer.writerows(mediumday2)
                    for exercise in mediumday2:
                        date,level,name,sets,reps,weight,duration,calories=exercise
                        print(f"{date} : {level} - {name} : {sets}sets*{reps}reps of {weight}, {duration}mins burning {calories}kcal")
            elif day==3:
                import csv
                with open("workouts.csv","a",newline="") as file:
                    writer=csv.writer(file)
                    writer.writerows(mediumday3)
                    for exercise in mediumday3:
                        date,level,name,sets,reps,weight,duration,calories=exercise
                        print(f"{date} : {level} - {name} : {sets}sets*{reps}reps of {weight}, {duration}mins burning {calories}kcal")
            elif day==4:
                import csv
                with open("workouts.csv","a",newline="") as file:
                    writer=csv.writer(file)
                    writer.writerows(mediumday4)
                    for exercise in mediumday4:
                        date,level,name,sets,reps,weight,duration,calories=exercise
                        print(f"{date} : {level} - {name} : {sets}sets*{reps}reps of {weight}, {duration}mins burning {calories}kcal")
            elif day==5:
                import csv
                with open("workouts.csv","a",newline="") as file:
                    writer=csv.writer(file)
                    writer.writerows(mediumday5)
                    for exercise in mediumday5:
                        date,level,name,sets,reps,weight,duration,calories=exercise
                        print(f"{date} : {level} - {name} : {sets}sets*{reps}reps of {weight}, {duration}mins burning {calories}kcal")
            elif day==6:
                import csv
                with open("workouts.csv","a",newline="") as file:
                    writer=csv.writer(file)
                    writer.writerows(mediumday6)
                    for exercise in mediumday6:
                        date,level,name,sets,reps,weight,duration,calories=exercise
                        print(f"{date} : {level} - {name} : {sets}sets*{reps}reps of {weight}, {duration}mins burning {calories}kcal")
            elif day==7:
                break
            else:
                print("Invalid Input")
    def advancedtemplate():
        print("hi")
    def selfworkouts():
        while True:
            print("Choose if you want to add Exercise")
            print("1 - ADD new Exercise")
            print("2 - Stop adding")
            sel=int(input("Choose what you want to do(1,2) :"))
            if sel==1:
                Exercise=input("Exercise: ")
                Sets=int(input("Sets: "))
                Reps=int(input("Reps: "))
                Weight_Lifted=int(input("Weight Lifted: "))
                Duration=int(input("Duration in minutes: "))
                Calories=int(input("Calories(kcal): "))
                import csv
                with open("workouts.csv","a",newline="") as file:
                    writer=csv.writer(file)
                    writer.writerow([today,"self",Exercise,Sets,Reps,Weight_Lifted,Duration,Calories])
            elif sel==2:
                break
            else:
                print("Invalid input")
        
    def suggestedworkouts():
        while True:
            print("Choose your Workout Template: ")
            print("1 - Beginner(1-6 months)")
            print("2 - Medium(6-12 months)")
            print("3 - Advanced(12-further months)")
            print("4 - GoBack")
            select=int(input("Choose the Template(1,2,3,4) : "))
            if select==1:
                beginnertemplate()
            elif select==2:
                mediumtemplate()
            elif select==3:
                advancedtemplate()
            elif select==4:
                break
            else:
                print("Invalid Input")
        
    while True:
        print("Choose one of the number: ")
        print("1 - SELF WORKOUTS")
        print("2 - SUGGESTED WORKOUTS")
        print("3 - Exit")
        choice=int(input("Fill Choice(1,2,3) : "))
        if choice==1:
            selfworkouts()
        elif choice==2:
            suggestedworkouts()
        elif choice==3:
            break
        else:
            print("Invalid Input")
        
    
