def analytics():
    def usersum():
        pass
    def nutrisum():
        pass
    def worksum():
        pass
    def bodyprogress():
        pass
    def goalprogress():
        pass
    def report():
        pass
    def recommendations():
        pass
    while True:
        print("="*10,"Analytics Dashboard","="*10)
        print("1 - User Summary")
        print("2 - Nutrition Analytics")
        print("3 - Workout Analytics")
        print("4 - Body Progress")
        print("5 - Goal Progress")
        print("6 - Weekly/Monthly Reports")
        print("7 - Recommendations")
        print("8 - Back")
        ana=int(input("Choose the function(1,2,3,4,5,6,7,8): "))
        if ana==1:
            usersum()
        elif ana==2:
            nutrisum()
        elif ana==3:
            worksum()
        elif ana==4:
            bodyprogress()
        elif ana==5:
            goalprogress()
        elif ana==7:
            recommendations()
        elif ana==6:
            report()
        elif ana==8:
            break
        else:
            print("Invalid Input")