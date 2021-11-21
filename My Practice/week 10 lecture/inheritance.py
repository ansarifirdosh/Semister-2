success = False

while success == False:
    try:
        radius=int(input("enter the radius: "))
        area=3.13*(radius)**2
        print(area)
        success=True

    except:
        print("wrong data.")
