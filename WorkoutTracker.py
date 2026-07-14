def workouttracker():

    def beginnertemplate():
        
    def mediumtemplate():

    def advancedtemplate():

    def selfworkouts():
        print("hello")
        from datetime import date
        today=date.today()
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
                with open("workouts.csv","a",newline="") as f:
                    writer=csv.writer(f)
                    writer.writerow([today,Exercise,Sets,Reps,Weight_Lifted,Duration,Calories])
        
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
        
    
