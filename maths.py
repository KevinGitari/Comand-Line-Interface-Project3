import random 
import time
from database import SessionLocal
from contender import User, Quiz

# The Python Operators I will be using
OPERATORS = ["+", "-", "*", "//", "/"]
MAX_OPERAND = 81
MIN_OPERAND = 9
NUM_QUESTIONS = 5

# Function to operate the calculations
def calculations():

    right_side = random.randint(MIN_OPERAND, MAX_OPERAND)
    left_side = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    expressions = f"{left_side} {operator} {right_side}"
    answer = eval(expressions)
    return expressions, answer

def start_quiz(): 
    
    db = SessionLocal() #creates a new database the session

    # Get the contendors name and save to database

    name = input("Enter your name: ")
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user) #refresh the contender's ID

    wrong_answer = 0 
    right_answer = 0

    print("Welcome to the Maths Quiz!")
    start_time = time.time() #start the time

#loop through a set number of questions
    for i in range(NUM_QUESTIONS):
        print("Question", i + 1)
        question, result = calculations() #genetate the question
        print(question)

        while True:
            answer = input("Enter your answer: ")
            try:
                user_answer = float(answer) #convert the answer given to float
                if round(user_answer, 2) == round(result, 2):
                    print("Correct!") #check if the answer is correct
                    right_answer += 1
                    break
                else:
                    print("Incorrect. Please try again.") #check if the answer is incorrect
                    wrong_answer += 1
            except ValueError:
                print("Please enter a valid number.") #check if the answer is a number

    end_time = time.time() #end the time
    time_taken = end_time - start_time # shows the total time taken

    # Save quiz result
    quiz = Quiz(score=right_answer, user_id=user.id)
    db.add(quiz)
    db.commit()

# print out the final result
    print(f"\nGame Over! Your score: {right_answer} correct, {wrong_answer} incorrect.")
    print(f"Time taken: {time_taken:.2f} seconds.")

    db.close() #callback function to close the session
#start_quiz()

