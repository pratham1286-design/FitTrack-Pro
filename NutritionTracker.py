def nutrition():
    def add_food():
        while True:
            from datetime import datetime
            now=datetime.now()
            date=now.strftime("%d-%m-%Y")
            time=now.strftime("%H:%M:%S")
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
        while True:
            from datetime import datetime
            now=datetime.now()
            date=now.strftime("%d-%m-%Y")
            time=now.strftime("%H:%M:%S")
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
                userdate=input("Enter date(dd-mm-yyyy): ")
                try:
                    datetime.strptime(userdate,"%d-%m-%Y")#for checking if date is valid
                except ValueError:
                    print("Invalid Date!,please enter a valid date in the format dd-mm-yyyy.")
                    continue
                found=False
                import csv
                with open("nutrition.csv","r") as sfile:
                    reader=csv.reader(sfile)
                    next(reader)#ignores header
                    for row in reader:
                        if row[0]==userdate:
                            print(row)
                            found=True
                if not found:
                    print("no food entry on this date")
            elif sea==3:
                break
            else:
                print("invalid input")
    def total_calories():
        from datetime import datetime
        import csv
        while True:
            choose=int(input("1 - Total Calories of Today / 2 - To See Total Calories of a particular date / 3 - Exit : "))
            if choose==1:
                from datetime import date
                today=date.today().strftime("%d-%m-%Y")
                with open("nutrition.csv","r") as file:
                    reader=csv.reader(file)
                    next(reader)
                    totalcals=0
                    found=False
                    for row in reader:
                        if row[0]==today:
                            totalcals+=float(row[6])
                            found=True
                if found:
                    print("Total Today's Calories",totalcals)
                else:
                    print("No Food Entry on this date")
            elif choose==2:
                newuserdate=input("Enter date(dd-mm-yyyy): ")
                try:
                    datetime.strptime(newuserdate,"%d-%m-%Y")#for checking if date is valid
                except ValueError:
                    print("Invalid Date!,please enter a valid date in the format dd-mm-yyyy.")
                    continue
                with open("nutrition.csv","r") as file:
                    reader=csv.reader(file)
                    next(reader)
                    totalcals=0
                    found=False
                    for row in reader:
                        if row[0]==newuserdate:
                            totalcals+=float(row[6])
                            found=True
                if found:
                    print("Total Calories: ",totalcals)
                else:
                    print("No Food Entry on this date")
            elif choose==3:
                break
            else:
                print("Invalid Input")
    def macros():
        from datetime import datetime
        import csv
        while True:
            choose=int(input("1 - Total of All Macros of Today / 2 - To See Total of All Macros of a particular date / 3 - Exit : "))
            if choose==1:
                from datetime import date
                today=date.today().strftime("%d-%m-%Y")
                with open("nutrition.csv","r") as file:
                    reader=csv.reader(file)
                    next(reader)
                    totalpro=0
                    totalcarbs=0
                    totalfats=0
                    found=False
                    for row in reader:
                        if row[0]==today:
                            totalpro+=float(row[7])
                            totalcarbs+=float(row[8])
                            totalfats+=float(row[9])
                            found=True
                if found:
                    while True:
                        print("choose what you want to Total of:")
                        print("1 - All")
                        print("2 - Protein")
                        print("3 - Carbs")
                        print("4 - Fats")
                        print("5 - Exit")
                        tot=int(input("choose between(1,2,3,4,5):"))
                        if tot==1:
                            print("Total Today's Protein",totalpro)
                            print("Total Today's Carbs",totalcarbs)
                            print("Total Today's Fats",totalfats)
                        elif tot==2:
                            print("Total Today's Protein",totalpro)
                        elif tot==3:
                            print("Total Today's Carbs",totalcarbs)
                        elif tot==4:
                            print("Total Today's Fats",totalfats)
                        elif tot==5:
                            break
                        else:
                            print("Invalid Input")
                else:
                    print("No Food Entry on this date")
            elif choose==2:
                newuserdate=input("Enter date(dd-mm-yyyy): ")
                try:
                    datetime.strptime(newuserdate,"%d-%m-%Y")#for checking if date is valid
                except ValueError:
                    print("Invalid Date!,please enter a valid date in the format dd-mm-yyyy.")
                    continue
                with open("nutrition.csv","r") as file:
                    reader=csv.reader(file)
                    next(reader)
                    totalpro=0
                    totalcarbs=0
                    totalfats=0
                    found=False
                    for row in reader:
                        if row[0]==newuserdate:
                            totalpro+=float(row[7])
                            totalcarbs+=float(row[8])
                            totalfats+=float(row[9])
                            found=True
                if found:
                    while True:
                        print("choose what you want to Total of:")
                        print("1 - All")
                        print("2 - Protein")
                        print("3 - Carbs")
                        print("4 - Fats")
                        print("5 - Exit")
                        tota=int(input("choose between(1,2,3,4,5):"))
                        if tota==1:
                            print("Total ",newuserdate," Protein",totalpro)
                            print("Total ",newuserdate," Carbs",totalcarbs)
                            print("Total ",newuserdate," Fats",totalfats)
                        elif tota==2:
                            print("Total ",newuserdate," Protein",totalpro)
                        elif tota==3:
                            print("Total ",newuserdate," Carbs",totalcarbs)
                        elif tota==4:
                            print("Total ",newuserdate," Fats",totalfats)
                        elif tota==5:
                            break
                        else:
                            print("Invalid Input")
                else:
                    print("No Food Entry on this date")
            elif choose==3:
                break
            else:
                print("Invalid Input")
    def protein_guide():
        protein_guide = {"Soya Chunks": 5.2,"Whey Protein": 8.0,"Chicken Breast": 3.1,"Peanuts": 2.6,
    "Fish": 2.3,
    "Almonds": 2.1,
    "Paneer": 1.9,
    "Tofu": 1.6,
    "Oats": 1.3,
    "Greek Yogurt": 1.0,
    "Dal": 0.5,
    "Rajma": 0.9,
    "Chole": 0.9,
    "Milk": 0.34,
    "Roti": 1.0,
    "Rice": 0.3
}

print(f"{'Food':<20}{'Protein/10 g'}")
print("-" * 35)

for food, protein in protein_guide.items():
    print(f"{food:<20}{protein}")
    while True:
        print("======NUTRITION======")
        print("1 - Add Food")
        print("2 - Search Food")
        print("3 - Total Calories")
        print("4 - Total Macros")
        print("5 - Protein Guide")
        print("6 - Exit")
        nut=int(input("Select the option(1,2,3,4,5,6,): "))
        if nut==1:
            add_food()
        elif nut==2:
            search_food()
        elif nut==3:
            total_calories()
        elif nut==4:
            macros()
        elif nut==5:
            protein_guide()
        elif nut==6:
            break
        else:
            print("Invalid Input")
