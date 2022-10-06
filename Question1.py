"""
Q1. Provide a program for the calculator from terminal.
• Make sure it do not ask questions but when you press enter. it displays the result.
• Amount and formula has to be in one line.
e.g 456 - 12
 564/ 10
 456*1234+09-12
"""

Calculator = input("Input for calculations: ") #input for operations of numbers
result = eval(Calculator) # using eval function
print(result) # printing the result