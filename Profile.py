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

    