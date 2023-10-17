print("Select an option")
print("1.Addition")
print("2.Subraction")
print("Multiplication")
print("Division")
while True:
#Take input from the user
    choice=input("Enter choice(1/2/3/4)")
    
    if choice in('1','2','3','4'):
        try:
            num1=float(input("enter first number"))
            num2=float(input("enter second number"))
        except ValueError:
            print("invalid input.Please enter a number.")
            continue 
        
        if choice=="1":
            print(num1,"+",num2,"=",num1+num2)
        elif choice=="2":
            print(num1,"-",num2,"=",num1-num2)
        elif choice=="3":
            print(num1,"*",num2,"=",num1*num2)
        elif choice=="4":
            print(num1,"/",num2,"=",(num1/num2))
        next_calculation=input("let's do the next calculation?(yes/No)")
        if next_calculation=="no":
            break
            
    else:
        print("Invalid input please enter a number")        
                           












