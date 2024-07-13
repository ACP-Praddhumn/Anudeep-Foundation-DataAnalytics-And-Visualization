num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))
num4 = int(input("Enter the forth number : "))
if(num1 == num2 and num1 == num3 and num1 == num4) : 
    print("All are equal")
# elif(num1 >= num2):
#     if(num1 > num3):
#         if(num1 > num4):
#             print("Greatest : ",num1)
#         else : 
#             print("Greatest : ",num4)
#     elif(num3 > num4) :
#         print("Greatest : ",num3)
#     else :
#         print("Greatest : ",num4)
# elif(num2 > num3) :
#     if(num2 > num4):
#             print("Greatest : ",num2)
#     else : 
#             print("Greatest : ",num4)
# elif(num3 > num4):
#      print("Greatest : ",num3)
# else :
#      print("Greatest : ",num4)


#another way
elif(num1>= num2 and num1 >= num3 and num1 >= num4) : 
    print("Greatest : ",num1)
elif (num2>= num3 and num2 >= num4):
    print("Greatest : ",num2)
elif(num3>= num4) : 
    print("Greatest : ",num3)
else :
    print("Greatest : ",num4)