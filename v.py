from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib import colors
import math

# Page dimensions
PAGE_WIDTH = 2480
PAGE_HEIGHT = 3508

# Margins
MARGIN_TOP = 400
MARGIN_BOTTOM = 200
MARGIN_LEFT = 200
MARGIN_RIGHT = 200

# Column dimensions
COLUMN_WIDTH = (PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT) // 5
COLUMN_HEIGHT = 581

# Number of questions
num_questions = int(input("Enter the number of questions: "))



# Calculate the number of columns needed
num_columns = math.ceil(num_questions / 10)

# Create a new PDF document
canvas = Canvas("columns.pdf", pagesize=portrait((PAGE_WIDTH, PAGE_HEIGHT)))

# Define the question and options
questions = [f"Question {i+1}" for i in range(num_questions)]
options = ["A", "B", "C", "D"]

# Draw columns and add questions with options in a reversed order
for i in range(num_columns - 1, -1, -1):
    # Calculate the position of each column
    column_x = MARGIN_LEFT + ((i % 5) * COLUMN_WIDTH)
    column_y = PAGE_HEIGHT - MARGIN_TOP - ((i // 5 + 1) * COLUMN_HEIGHT)

    # Set the starting position for the questions
    question_x = column_x + 10
    question_y = column_y + COLUMN_HEIGHT - 20

    # Calculate the number of questions in the current column
    questions_in_column = min(10, num_questions - (i * 10))

    # Add questions and options
    for j in range(questions_in_column):
        # Calculate the position of each question
        current_question_x = question_x
        current_question_y = question_y - ((j + 1) * 55)  # Shift all question numbers down by one row

        # Draw the question number
        question_number = i * 10 + j + 1  # Start the question number from 1
        canvas.setFont("Helvetica", 12)
        canvas.drawString(current_question_x, current_question_y, f"{question_number}.")

        # Add the options
        for k, option in enumerate(options):
            option_x = current_question_x + 50 + (k * 60)
            option_y = current_question_y - 30

            # Draw the bubble option circle
            canvas.setStrokeColor(colors.black)
            canvas.setFillColor(colors.white)
            canvas.circle(option_x, option_y, 10, fill=1, stroke=1)

            # Add the option label
            canvas.setFillColor(colors.black)
            canvas.setFont("Helvetica", 10)
            canvas.drawString(option_x - 5, option_y + 15, option)

# Save and close the PDF document
canvas.save()
