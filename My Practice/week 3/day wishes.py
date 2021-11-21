'''Write a program that asks the user to input the current day of the week, if 
it’s a weekday the program should print out “Happy weekday! Work 
hard!” else the output should be “Enjoy your weekend!”.'''

#Asking user to input the day
day=input("Enter what is the day today: ").lower()

#using if else statement
if day=="saturday" or day=="sunday":
    print("Enjoy your weekend!")

elif day=="monday" or day=="tuesday" or day=="wednesday" or day=="thursday" or day=="friday":
    print("Happy week day.work hard!")

else:
    print("Please enter the valid day")

