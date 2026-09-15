num1 = int(input("Enter the first number: "))

print("""
What do you want to do?
1. Add
2. Subtract
3. Multiply
4. Divide""")
response = input("Enter 1-4: ")
response = int(response)-1

operator = ["+", "-", "x", "/"]
operator = operator[response] 


num2 = int(input("\nEnter the second number: "))

if operator == "+":
  answer = num1+num2
elif operator == "-":
  answer = num1-num2
elif operator == "x":
  answer = num1*num2
else:
  answer = num1/num2
  
print("{}{}{} = {}".format(num1, operator, num2, answer))