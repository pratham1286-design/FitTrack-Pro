def userinfo():
    Name=input("Enter Name: ")
    Age=int(input("Enter Age: "))
    gender=int(input("GENDER: 1 for male OR 2 for female:"))
    if gender==1:
        gender="Male"
    elif gender==2:
        gender="Female"
    else:
        print("invalid input")
    print(gender)
    Height=int(input("Height(cm): "))
    Weight=int(input("Current Weight(kgs): "))
    Goal_Weight=int(input("Goal Weight(kgs): "))
    FitnessGoal=int(input("FITNESS GOAL: 1 for Lose Fat , 2 for Muscle Building , 3 for Maintaining Weight :"))
    if FitnessGoal==1:
        FitnessGoal="Lose Fat"
    elif FitnessGoal==2:
        FitnessGoal="Muscle Building"
    elif FitnessGoal==3:
        FitnessGoal="Maintaining Weight"
    else:
        FitnessGoal="Muscle Building"
        print("invalid input")
    from datetime import date
    today=date.today()
    new_row=[today,Name,Age,gender,Height,Weight,Goal_Weight,FitnessGoal]
    import csv
    with open("userinfo.csv","w") as file:
        writer=csv.writer(file)
        writer.writerows(new_row)
    print("Saved User Data Successfully")