
# answer = input("Choose \n1 to convert km -> miles:  \n2 to convert miles -> km: ")
# if answer == "1":
#     km = float(input("Enter km :"))
#     miles = km * 1.609
#     print(miles, "miles")
# elif answer == "2":
#     ml = float(input("Enter miles :"))
#     km = ml / 1.609
#     print(km, "km")
# else:
#     print("Wrong input please try again!")

# a = input("Choose: \n1 to convert Celsius -> Fahrenheit:  \n2 to convert Fahrenheit -> Celsius: ")
# if a == "1":
#     c = float(input("Enter Celsius :"))
#     f = (c * 9/5) + 32
#     print(f, "Fahrenheit")
# elif a == "2":
#     f = float(input("Enter Fahrenheit :"))
#     c = (f - 32) * 5/9
#     print(c, "Celsius")
# else:
#     print("Wrong input please try!!!!!!")
# for number in range(3, 15):
#     print(number)
# name = "tanya"
# for a in name:
#     print(a)
# i = 20
# while i>1:
#     i -= 1
#     if i == 14:
#         continue
#     print (i)
def print_result(result):


    print("Result :" + str(result))
one = int(input( "Enter a number:"))
two = int(input( "Enter a number:"))

result = one + two
print_result(result)

result = one - two
print_result(result)

result = one * two
print_result(result)

result = one / two
print_result(result)

