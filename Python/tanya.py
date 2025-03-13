#print("Tanan")
answer = input("Choose \n1 to convert km -> miles:  \n2 to convert miles -> km: ")
if answer == "1":
    km = float(input("Enter km :"))
    miles = km * 1.609
    print(miles, "miles")
elif answer == "2":
    ml = float(input("Enter miles :"))
    km = ml / 1.609
    print(km, "km")
else:
    print("Wrong input please try again!")

