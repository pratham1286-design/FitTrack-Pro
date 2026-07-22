print("="*55)
print("                 FIT TRACK PRO")
print("         Personal Fitness Management System")
print("="*55)
while True:
    print("Choose the function:--")
    print("1 - Use the Functions in an order")
    print("2 - User Profile")
    print("3 - Workout Manager")
    print("4 - Nutrition Tracker")
    print("5 - Fitness Tools")
    print("6 - Analytics Dashboard")
    print("7 - break")
    main=int(input("Choose between (1,2,3,4,5,6,7):"))
    if main==1:
        from Profile import userinfo
        userinfo()
        from WorkoutTracker import workouttracker
        workouttracker()
        from NutritionTracker import nutrition
        nutrition()
        from Tools import Tools
        Tools()
        from AnalyticsDashboard import analytics
        analytics()
    elif main==2:
        from Profile import userinfo
        userinfo()
    elif main==3:
        from WorkoutTracker import workouttracker
        workouttracker()
    elif main==4:
        from NutritionTracker import nutrition
        nutrition()
    elif main==5:
        from Tools import Tools
        Tools()
    elif main==6:
        from AnalyticsDashboard import analytics
        analytics()
    elif main==7:
        break
    else:
        print("Invalid Input")