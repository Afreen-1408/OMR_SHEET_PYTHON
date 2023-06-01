from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib import colors

# Page dimensions
PAGE_WIDTH = 2480
PAGE_HEIGHT = 3508

# Margins
MARGIN_TOP = 150
MARGIN_BOTTOM = 200
MARGIN_LEFT = 200
MARGIN_RIGHT = 200

# Section dimensions
SECTION_WIDTH = 520
SECTION_HEIGHT = PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM - 800

# Column dimensions
LEFT_COLUMN_WIDTH = 520
RIGHT_COLUMN_WIDTH = 1150
COLUMN_HEIGHT = 550

# Bubble options
OPTIONS = ["A", "B", "C", "D", "E"]
BUBBLE_RADIUS = 10
BUBBLE_GAP = 10
LABEL_GAP = 10
NUMBERING_GAP = 20

# Create a new PDF document
canvas = Canvas("omr_sheet.pdf", pagesize=portrait((PAGE_WIDTH, PAGE_HEIGHT)))

# Draw the left column
left_column_x = MARGIN_LEFT
left_column_y = PAGE_HEIGHT - MARGIN_TOP - COLUMN_HEIGHT - 100
canvas.rect(left_column_x, left_column_y, LEFT_COLUMN_WIDTH, COLUMN_HEIGHT)

# Add the question numbers and options in the left column
question_x = left_column_x + 10
question_y = left_column_y + COLUMN_HEIGHT - 20 - NUMBERING_GAP

num_questions = 10
num_options = 4

for question in range(num_questions):
    question_number = question

    canvas.setFont("Helvetica", 15)
    canvas.drawString(question_x, question_y - question * 45 - NUMBERING_GAP, f"{question_number}.")

    for k in range(num_options):
        if k >= len(OPTIONS):
            break

        option = OPTIONS[k]
        bubble_x = question_x + 40 + (k * 60) + NUMBERING_GAP
        bubble_y = question_y - question * 45 - 30

        # Draw the bubble option circle
        canvas.setStrokeColor(colors.black)
        canvas.setFillColor(colors.white)
        bubble_center_x = bubble_x + BUBBLE_RADIUS
        bubble_center_y = bubble_y + BUBBLE_RADIUS
        canvas.circle(bubble_center_x, bubble_center_y, BUBBLE_RADIUS, fill=1, stroke=1)

        # Add the option label
        canvas.setFillColor(colors.black)
        canvas.setFont("Helvetica", 15)
        label_x = bubble_center_x
        label_y = bubble_center_y + BUBBLE_RADIUS + LABEL_GAP
        canvas.drawCentredString(label_x, label_y, option)


right_column_x = left_column_x + LEFT_COLUMN_WIDTH + 400
right_column_y = left_column_y
canvas.rect(right_column_x, right_column_y, RIGHT_COLUMN_WIDTH, COLUMN_HEIGHT)

# Add labels in the top-right column with increased font size and margin
label_x = right_column_x + 50
label_y = right_column_y + COLUMN_HEIGHT - 20 - NUMBERING_GAP
label_gap = 120

canvas.setFont("Helvetica", 40)  # Change font size to 20px
canvas.drawString(label_x, label_y - label_gap, "NAME:")
canvas.drawString(label_x, label_y - 2 * label_gap, "EXAM:")
canvas.drawString(label_x, label_y - 3 * label_gap, "DATE:")


# Prompt the user for the number of sections
num_sections = int(input("Enter the number of sections: "))

# Validate the number of sections
if num_sections > 4:
    print("Error: Maximum number of sections allowed is 4")
    canvas.save()
    exit()

# Draw the sections
for section in range(num_sections):
    # Calculate the position of each section
    section_x = MARGIN_LEFT + section * SECTION_WIDTH
    section_y = MARGIN_BOTTOM + 100

    # Draw the section rectangle
    canvas.rect(section_x, section_y, SECTION_WIDTH, SECTION_HEIGHT)

    # Prompt the user for the number of questions in this section
    num_questions = int(input(f"Enter the number of questions for Section {section + 1}: "))

    # Validate the number of questions
    if num_questions > 50:
        print("Error: Maximum number of questions allowed is 50")
        canvas.save()
        exit()

    # Prompt the user for the number of bubble options for this section
    num_options = int(input(f"Enter the number of bubble options for Section {section + 1}: "))

    # Validate the number of bubble options
    if num_options < 2:
        print("Error: Minimum number of bubble options allowed is 2")
        canvas.save()
        exit()
    elif num_options > 5:
        print("Error: Maximum number of bubble options allowed is 5")
        canvas.save()
        exit()

    # Add the question numbers and options
    question_x = section_x + 10
    question_y = section_y + SECTION_HEIGHT - 20 - NUMBERING_GAP

    for question in range(num_questions):
        question_number = section * num_questions + question + 1

        canvas.setFont("Helvetica", 15)
        canvas.drawString(question_x, question_y - question * 45 - NUMBERING_GAP, f"{question_number}.")

        # Add the gap after each question
        canvas.setStrokeColor(colors.white)
        canvas.setFillColor(colors.white)
        canvas.rect(
            question_x - 2,  # Left coordinate
            question_y - question * 45 - NUMBERING_GAP - 20,  # Bottom coordinate
            SECTION_WIDTH - 6,  # Width
            2,  # Height
            fill=True,
            stroke=False,
        )

        for k in range(num_options):
            if k >= len(OPTIONS):
                break

            option = OPTIONS[k]
            bubble_x = question_x + 40 + (k * 60) + NUMBERING_GAP
            bubble_y = question_y - question * 45 - 30

            # Draw the bubble option circle
            canvas.setStrokeColor(colors.black)
            canvas.setFillColor(colors.white)
            bubble_center_x = bubble_x + BUBBLE_RADIUS
            bubble_center_y = bubble_y + BUBBLE_RADIUS
            canvas.circle(bubble_center_x, bubble_center_y, BUBBLE_RADIUS, fill=1, stroke=1)

            # Add the option label
            canvas.setFillColor(colors.black)
            canvas.setFont("Helvetica", 15)
            label_x = bubble_center_x
            label_y = bubble_center_y + BUBBLE_RADIUS + LABEL_GAP
            canvas.drawCentredString(label_x, label_y, option)

# Save and close the PDF document
canvas.save()
