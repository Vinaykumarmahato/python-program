print('''
      + addition
      _ subtraction
      * multiple
      / division
      
      '''
      )

vinay=int(input("enter your first value  : "))
shahnaj=int(input("enter your second number  : "))
banti=input("enter the operation")

if banti=="+":
    print(vinay+shahnaj)
elif banti=="-":
    print(vinay+shahnaj)
elif banti=="*":
    print(vinay/shahnaj)
else:
    print("ENVALID DATA")