# exception-handling.py
print("Begin")
i=input("Enter first number")
j=input("Enter second number")
try:
  x=int(i)
  y=int(j)
  z=x/y
  print(z)
except:
  print("Error Occured")
print("end")
