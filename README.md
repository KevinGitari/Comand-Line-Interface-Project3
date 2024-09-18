### MY PHASE3 PROJECT (A MATH GAME CHALLENGE) 

### Command Line Interface (PYTHON)
   
   # OVERVIEW 
The Math Quiz Game is a command line application that challenges the contenders with some random mathematical quizes whilst tracking their scores.
It utilizes SQLAlchemy for Object-Relational Mapping (ORM) to manage user data and quiz results, storing them in a SQLite database.

## THE FEATURES
**Interactive Quiz**: Contendors answer random mathematical quizes generated from different operators.
- **Score Tracking**: The application keeps track of correct and incorrect answers.
- **Database Storage**: The contendors information and quiz scores are stored in a SQLite database.
- **ORM Implementation**: Utilizes SQLAlchemy to perform CRUD operations on the contendors data and quiz results.

  ## GETTING STARTED

### Prerequisites
 -Python 3.10.12
- pip (Python package installer)

## Installation
**Clone the repository**:
   ```bash
   git clone https://github.com/KevinGitari/Comand-Line-Interface-Project3
   ```

2. **Set up a virtual environment**:
   ```bash
   pip install pipenv
   pipenv install
   ```

3. **Install required packages**:
   ```bash
   pipenv install SQLAlchemy
   ```

### Running the Application
1. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

2. Start the CLI:
   ```bash
   python cli.py
   ```

### The Database
The application uses SQLite for storing contendors data and quiz scores. The database schema is automatically created when you run the application for the first time.

### My Code Structure
- **`cli.py`**: Main entry point for the command-line interface.
- **`math.py`**: Contains the quiz logic and calculations.
- **`models.py`**: Defines the database models (User and Quiz).
- **`database.py`**: Handles database connections and table_creation.

### License
This project is licensed under the MIT License. See the LICENSE file for detail





