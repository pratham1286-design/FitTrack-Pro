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
    import pandas as pd 
    df=pd.read_csv("userinfo.csv")
    new_row={"Date":today,"Name":Name,"Age":Age,"Gender":gender,"Height":Height,"Weight":Weight,"Goal Weight":Goal_Weight,"Fitness Goal":FitnessGoal}
    df.loc[len(df)]=new_row
    df.to_csv("userinfo.csv",index=False)