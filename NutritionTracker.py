def nutrition():
    def add_food():
        from datetime import datetime
        now=datetime.now()
        date=now.strftime("%d-%m-%Y")
        time=now.strftime("%H:%M:%S")
        while True:
            Type=int(input("1 - Breakfast/2 - Lunch/3 - Dinner/4 - Exit: "))
            if Type==1:
                break_food=input("Add Breakfast: ")
                bquantity=int(input("Food Quantity: "))
                bunit=input("give unit for food: ")
                bcalories=int(input("Add Calories: "))
                bprotein=int(input("Add Protein: "))
                bCarbs=int(input("Add Carbs: "))
                bFat=int(input("Add Fat: "))
                import csv
                with open("nutrition.csv","a",newline="") as nfile:
                    writer=csv.writer(nfile)
                    writer.writerow([date,time,"Breakfast",break_food,bquantity,bunit,bcalories,bprotein,bCarbs,bFat])
                print("Added Food: ",break_food,",Quantity: ",bquantity,bunit,",Calories: ",bcalories,",protein: ",bprotein,"g",",Carbs: ",bCarbs,"g",",Fat: ",bFat)
            elif Type==2:
                lunch_food=input("Add Lunch: ")
                lquantity=int(input("Food Quantity: "))
                lunit=input("give unit for food: ")
                lcalories=int(input("Add Calories: "))
                lprotein=int(input("Add Protein: "))
                lCarbs=int(input("Add Carbs: "))
                lFat=int(input("Add Fat: "))
                import csv
                with open("nutrition.csv","a",newline="") as lfile:
                    writer=csv.writer(lfile)
                    writer.writerow([date,time,"Lunch",lunch_food,lquantity,lunit,lcalories,lprotein,lCarbs,lFat])
                print("Added Food: ",lunch_food,",Quantity: ",lquantity,lunit,",Calories: ",lcalories,",protein: ",lprotein,"g",",Carbs: ",lCarbs,"g",",Fat: ",lFat)
            elif Type==3:
                dinner_food=input("Add Dinner: ")
                dquantity=int(input("Food Quantity: "))
                dunit=input("give unit for food: ")
                dcalories=int(input("Add Calories: "))
                dprotein=int(input("Add Protein: "))
                dCarbs=int(input("Add Carbs: "))
                dFat=int(input("Add Fat: "))
                import csv
                with open("nutrition.csv","a",newline="") as dfile:
                    writer=csv.writer(dfile)
                    writer.writerow([date,time,"Dinner",dinner_food,dquantity,dunit,dcalories,dprotein,dCarbs,dFat])
                print("Added Food: ",dinner_food,",Quantity: ",dquantity,dunit,",Calories: ",dcalories,",protein: ",dprotein,"g",",Carbs: ",dCarbs,"g",",Fat: ",dFat)
            elif Type==4:
                break
            else :
                print("Invalid Input")
    def search_food():
        from datetime import datetime
        now=datetime.now()
        date=now.strftime("%d-%m-%Y")
        time=now.strftime("%H:%M:%S")
        while True:
            print("Choose the option :-")
            print("1 - Search by FOOD NAME")
            print("2 - Search by DATE")
            print("3 - EXIT")
            sea=int(input("Choose what you want to do(1,2,3): "))
            if sea==1:
                food=input("Enter Food name to search: ").lower()
                found=False
                import csv
                with open("nutrition.csv","r") as sfile:
                    reader=csv.reader(sfile)
                    next(reader)#ignores header
                    for row in reader:
                        if food in row[3].lower():
                            print("-"*25)
                            print("Date: ",row[0])
                            print("Time: ",row[1])
                            print("Meal: ",row[2])
                            print("Food: ",row[3])
                            print("Quantity: ",row[4],row[5])
                            print("Calories: ",row[6])
                            print("Protein: ",row[7],"g")
                            print("Carbs: ",row[8],"g")
                            print("Fat: ",row[9],"g")
                            print("-"*25)
                            found=True
                if not found:
                    print("Food not found")
            elif sea==2:
                date=input("Enter date(dd-mm-yyyy): ")
                try:
                    datetime.strptime(date,"%d-%m-%Y")#for checking if date is valid
                except ValueError:
                    print("Invalid Date!,please enter a valid date in the format dd-mm-yyyy.")
                    return
                found=False
                import csv
                with open("nutrition.csv","r") as sfile:
                    reader=csv.reader(sfile)
                    next(reader)#ignores header
                    for row in reader:
                        if row[0]==date:
                            print(row)
                            found=True
                if not found:
                    print("no food entry on this date")
            elif sea==3:
                break
            else:
                print("invalid input")
    def delete_food():
        pass
    def total_calories():
        pass
    def macros():
        pass
    def protein_guide():
        pass
    while True:
        print("======NUTRITION======")
        print("1 - Add Food")
        print("2 - Search Food")
        print("3 - Delete Food")
        print("4 - Total Calories")
        print("5 - Total Macros")
        print("6 - Protein Guide")
        print("7 - Exit")
        nut=int(input("Select the option(1,2,3,4,5,6,7): "))
        if nut==1:
            add_food()
        elif nut==2:
            search_food()
        elif nut==3:
            delete_food()
        elif nut==4:
            total_calories()
        elif nut==5:
            macros()
        elif nut==6:
            protein_guide()
        elif nut==7:
            break
        else:
            print("Invalid Input")
