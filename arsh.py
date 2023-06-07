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
SECTION_HEIGHT = (PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM - 1150) // 6


# Gap between sections and columns
SECTION_GAP = 20
COLUMN_GAP = 20

# Bubble options
OPTIONS = ["A", "B", "C", "D"]
BUBBLE_RADIUS = 12
BUBBLE_GAP = 30
LABEL_GAP = 5
NUMBERING_GAP = 20



# Column dimensions
LEFT_COLUMN_WIDTH = 520
RIGHT_COLUMN_WIDTH = 1200
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

# Draw the four small columns above the left column
small_column_width = 20
small_column_height = 20
small_column_x = left_column_x + BUBBLE_RADIUS - small_column_width // 2 + 80 # Add a gap of 40 pixels

for _ in range(4):
    small_column_y = left_column_y + COLUMN_HEIGHT + BUBBLE_GAP - small_column_height + 40
    canvas.rect(small_column_x, small_column_y, small_column_width, small_column_height)
    small_column_x += (2 * BUBBLE_RADIUS) + BUBBLE_GAP + 28  # Add a gap of 40 pixels

# Add the "Roll No:" label on the left side
roll_label_x = left_column_x - (-10)
roll_label_y = left_column_y + COLUMN_HEIGHT + 30  # Add a gap of 40 pixels
canvas.setFont("Helvetica", 15)
canvas.drawString(roll_label_x, roll_label_y, "Roll No:")



# Draw the right column
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


# Save and close the PDF document
canvas.save()

