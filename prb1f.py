try:
 a=int(input("Enter first value:"))
 b=int(input("Enter second value:"))
 
 print("Result:",a/b)
except ZeroDivisionError:
 print("Can't divide by zero")
except ValueError:
 print("Plese Enter integer value")  

