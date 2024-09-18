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
    db = SessionLocal()

    name = input("Enter your name: ")
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)

    wrong_answer = 0
    right_answer = 0

    print("Welcome to the Maths Quiz!")
    start_time = time.time()

    for i in range(NUM_QUESTIONS):
        print("Question", i + 1)
        question, result = calculations()
        print(question)

        while True:
            answer = input("Enter your answer: ")
            try:
                user_answer = float(answer)
                if round(user_answer, 2) == round(result, 2):
                    print("Correct!")
                    right_answer += 1
                    break
                else:
                    print("Incorrect. Please try again.")
                    wrong_answer += 1
            except ValueError:
                print("Please enter a valid number.")

    end_time = time.time()
    time_taken = end_time - start_time

    # Save quiz result
    quiz = Quiz(score=right_answer, user_id=user.id)
    db.add(quiz)
    db.commit()

    print(f"\nGame Over! Your score: {right_answer} correct, {wrong_answer} incorrect.")
    print(f"Time taken: {time_taken:.2f} seconds.")

    db.close()
