#write program to input first & last name and display reverse name

firstN=input("Enter your first name = ")
lastN=input("Enter your last name = ")
firstN,lastN = lastN,firstN
print("Reverse Name ",firstN," ",lastN)