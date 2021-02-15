input1 = int(input("Enter number-->"))
try:
   val = int(input1)
except ValueError:
   print("That's not an int!")
operator =  input("Enter Operator-->")
input2 = int(input("Enter another number-->"))
try:
   val = int(input2)
except ValueError:
   print("That's not an int!")
if operator == "+":
    print(input1 + input2)
elif operator == "-":
    print(input1 - input2)
elif operator == "*":
    print(input1 * input2)
elif operator == "/":
    print(input1 / input2)
else:
    print("Please enter correct operator only")


