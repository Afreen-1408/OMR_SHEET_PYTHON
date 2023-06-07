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
OPTIONS = ["A", "B", "C", "D"]
BUBBLE_RADIUS = 10
BUBBLE_GAP = 10
LABEL_GAP = 5
NUMBERING_GAP = 20

# Create a new PDF document
canvas = Canvas("omr_sheet.pdf", pagesize=portrait((PAGE_WIDTH, PAGE_HEIGHT)))

# Draw the left column
left_column_x = MARGIN_LEFT
left_column_y = PAGE_HEIGHT - MARGIN_TOP - COLUMN_HEIGHT - 100
canvas.rect(left_column_x, left_column_y, LEFT_COLUMN_WIDTH, COLUMN_HEIGHT)

# Draw the right column
right_column_x = left_column_x + LEFT_COLUMN_WIDTH + 400
right_column_y = left_column_y
canvas.rect(right_column_x, right_column_y, RIGHT_COLUMN_WIDTH, COLUMN_HEIGHT)

# Draw four sections
for i in range(4):
    # Calculate the position of each section
    section_x = MARGIN_LEFT + i * SECTION_WIDTH
    section_y = MARGIN_BOTTOM + 100

    # Draw the section rectangle
    canvas.rect(section_x, section_y, SECTION_WIDTH, SECTION_HEIGHT)

    # Add the question numbers and options
    question_x = section_x + 10
    question_y = section_y + SECTION_HEIGHT - 20 - NUMBERING_GAP

    for j in range(50):
        question_number = i * 50 + j + 1
        canvas.setFont("Helvetica", 12)
        canvas.drawString(question_x, question_y - j * 45 - NUMBERING_GAP, f"{question_number}.")

        for k, option in enumerate(OPTIONS):
            bubble_x = question_x + 40 + (k * 60) + NUMBERING_GAP
            bubble_y = question_y - j * 45 - 30

            # Draw the bubble option circle
            canvas.setStrokeColor(colors.black)
            canvas.setFillColor(colors.white)
            bubble_center_x = bubble_x + BUBBLE_RADIUS
            bubble_center_y = bubble_y + BUBBLE_RADIUS
            canvas.circle(bubble_center_x, bubble_center_y, BUBBLE_RADIUS, fill=1, stroke=1)

            # Add the option label
            canvas.setFillColor(colors.black)
            canvas.setFont("Helvetica", 10)
            label_x = bubble_center_x
            label_y = bubble_center_y + BUBBLE_RADIUS + LABEL_GAP
            canvas.drawCentredString(label_x, label_y, option)

# Save and close the PDF document
canvas.save()
