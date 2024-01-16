# Write a python program for the following:
#Input the string “Python” as a list of characters from console, delete at least 2 characters, reversethe resultant string and print it.

s1 = input("Enter the string :")
s2 =list(s1.strip())
print(type(s1))
print(s2)
s2.pop(-3)
s2.pop(-3)
print(s2)
s2.reverse()
s1 = ''.join(s2)
print(s1)


#Take two numbers from user and perform at least 4 arithmetic operations on them.

num1 = int(input("Enter the first number: ")) # user input1
num2 = int(input("Enter the second number: ")) # user input2

#Printing the result for 4 arithmetic operations
print("Addition: ",num1+num2) # simple Addition
print("Subraction: ", num1 - num2) # Subraction
print("Division: ",num1/num2) # simple Division
print("Floor Division: ",num1// num2) # floor Division

#Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’.
# declaring a string variable
temp = input("Enter the sentence :")

# replacing string python with pythons
temp = temp.replace('python', 'pythons')
print("Updated string is : ")
print(temp)

#Use the if statement conditions to write a program to print the letter grade based on an input class score. Use the grading scheme we are using in this class.

marks = int(input("Enter the marks of the person: "))
if marks >= 90:
    print("A grade")
elif marks >=80:
    print("B grade")
elif marks >=70:
    print("C grade")
elif marks >= 60:
    print("D grade")
else:
    print("Fail grade")
