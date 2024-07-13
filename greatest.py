#input of numbers
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

# No data validation required further

#multiple dependent condtions
if(num1 > num2) :
    print(num1, " is the gratest number")
elif(num1 < num2) : 
    print(num2, " is the gratest number")
else : 
    print("Both are the gratest number")