def nutrition():
    from datetime import datetime
    now=datetime.now()
    date=now.strftime("%d-%m-%Y")
    time=now.strftime("%H:%M:%S")
    
    def add_food():
        while True:
            Type=int(input("1 - Breakfast/2 - Lunch/3 - Dinner/4 - Exit: "))
            if Type==1:
                break_food=input("Add breakfast: ")
                quantity=int(input("Food Quantity: "))
                calories=int(input("Add Calories: "))
                protein=int(input("Add Protein: "))
                Carbs=int(input("Add Carbs: "))
                Fat=int(input("Add Fat: "))
                import csv
                with open("nutrition.csv","a",newline="") as file:
                    writer=csv.writer(file)
                    writer.writerow([date,time,"Breakfast",break_food,quantity,"g",calories,protein,Carbs,Fat])
    def search_food():
        pass
    def delete_food():
        pass
    def total_calories():
        pass
    def marcos():
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
            marcos()
        elif nut==6:
            protein_guide()
        elif nut==7:
            break
        else:
            print("Invalid Input")
