from maths import start_quiz
from database import create_tables

def main():
    create_tables()
    print("Welcome to the Math Quiz CLI!")
    start_quiz()

main() 
