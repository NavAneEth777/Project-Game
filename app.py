from flask import Flask, render_template, request
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
import math

# creating a flask app..
app = Flask(__name__) 

# Database
# engine = create_engine('sqlite:///database.db')  # Type of database
# Base = declarative_base()

# a model with
# class PerfectSquares(Base):
#     __tablename__ = 'perfect_squares'

#     id = Column(Integer, primary_key=True)
#     lower_bound = Column(Integer)
#     upper_bound = Column(Integer)
#     perfect_squares_list = Column(String)  # Comma-separated perfect squares
#     non_perfect_squares_list = Column(String)  # Comma-separated non-perfect squares

#     def __repr__(self):
#         return f"<PerfectSquares(id={self.id}, lower_bound={self.lower_bound}, upper_bound={self.upper_bound}, perfect_squares='{self.perfect_squares_list}', non_perfect_squares='{self.non_perfect_squares_list}')>"

# # Create database tables (if using the model)
# Base.metadata.create_all(engine)

# # Database session
# Session = sessionmaker(bind=engine)
# session = Session()


# Function to check if a number is a perfect square
def is_perfect_square(num):
    if num < 0:
        return False
    result = math.sqrt(num).is_integer()
    return result


def find_perfect_squares(lower, upper):
    """Finds perfect and non-perfect squares within the given range."""
    all_numbers = [num for num in range(lower, upper + 1)]
    perfect_squares = [num for num in all_numbers if is_perfect_square(num)]
    non_perfect_squares = [num for num in all_numbers if num not in perfect_squares]
    return perfect_squares, non_perfect_squares


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lower_bound = int(request.form['lower_bound'])
        upper_bound = int(request.form['upper_bound'])

        # Find perfect and non-perfect squares
        perfect_squares, non_perfect_squares = find_perfect_squares(lower_bound, upper_bound)

        # Optionally, store data in the database
        # new_record = PerfectSquares(lower_bound=lower_bound, upper_bound=upper_bound,
        #                             perfect_squares_list=','.join(map(str, perfect_squares)),
        #                             non_perfect_squares_list=','.join(map(str, non_perfect_squares)))
        # session.add(new_record)
        # session.commit()

        return render_template('index.html', perfect_squares=perfect_squares,
                                non_perfect_squares=non_perfect_squares, lower_bound=lower_bound, upper_bound=upper_bound)
    else:
        return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
