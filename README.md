# Perfect Squares Finder with Gate Visualization
This project implements a Flask application that finds perfect squares within a specified range and visualizes them as "open" gates, while non-perfect squares are represented as "closed" gates.

## Features:

 - User-friendly interface to enter a lower and upper bound.
- Calculates perfect squares within the given range.
- Displays the list of perfect squares found.
- Visualizes the numbers as gates:
    - Opened gates: Represent perfect squares.
    - Closed gates: Represent non-perfect squares.

 ## Requirements:

 - Python 3.x
- Flask
- SQLAlchemy (optional, for database storage)

## Setup:

1. Create a virtual environment (recommended) to isolate project dependencies:
```
python -m venv venv  # Create a virtual environment named 'venv'
source venv/bin/activate  # Activate on Linux/macOS
venv\Scripts\activate.bat  # Activate on Windows
```

2. Install required packages:

 ```Bash
pip install Flask SQLAlchemy
```
3. Clone or download this repository.

## Database (Optional):

This project can optionally store user input and results in a database using SQLAlchemy. If you choose to use a database, replace the database configuration in ```app.py``` with your credentials.

## Running the Application:

1. Navigate to the project directory in your terminal.

2. Activate the virtual environment (if used).

3. Run the Flask development server:

```Bash
python app.py runserver
```

4. Open ```http://127.0.0.1:5000/``` in your web browser to access the application.

## Usage:

1. Enter a lower and upper bound in the respective fields.
2. Click the "Find Perfect Squares" button.
3. The application will display the list of perfect squares found and the gate visualization.
