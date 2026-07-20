def Tools():
    import csv
    def bmi():
        while True:
            
            with open("userinfo.csv","r") as file:
                reader=csv.DictReader(file)
                for row in reader:
                    height_cm=float(row["Height"])
                    weight=float(row["Weight"])
                height_m=height_cm/100
                bmi=weight/(height_m**2)
                print("Your BMI: ",bmi)
    def bmr():
        pass
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
