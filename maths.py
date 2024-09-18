import random
from unittest import result

# The Python Operators I will be uising

OPERATORS = ["+", "-", "*", "//"]
MAX_OPERAND = 81
MIN_OPERAND = 9
NUM_QUESTIONS = 55

# writing a function to operate the calculations

def calculations():
    right_side = random.randint(MIN_OPERAND, MAX_OPERAND) # this will generate a random number between 9 and 81
    left_side = random.randint(MIN_OPERAND, MAX_OPERAND)
    operators = random.choice(OPERATORS)

    expressions = f"{left_side}  {operators}  {right_side}" # this is the string that will be evaluated
    answer = eval(expressions) # this will evaluate the string and return the result
    result = eval(expressions) # this will evaluate the string and return the result

    print(expressions, "=", result)# this will print the expression and the result
    return expressions

for i in range(NUM_QUESTIONS): #prints the number of questions
    print("Question", i+1)# prints the question number
    print("Question", calculations())# prints the answer
    while True: # this will loop the questions
        answer = input("Enter your answer: ") # this will ask for the answer
        if answer == str(result): # this will check if the answer is correct
            print("Correct!") # this will print correct
            break # this will break the loop
        else:
            print("Incorrect.Please try again to continue!.") # this will print incorrect and ask again
    calculations()

calculations()
    

