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
SECTION_HEIGHT = (PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM - 800) // 6

# Column dimensions
COLUMN_WIDTH = 520
COLUMN_HEIGHT = SECTION_HEIGHT

# Gap between sections and columns
SECTION_GAP = 20
COLUMN_GAP = 20

# Bubble options
OPTIONS = ["A", "B", "C", "D"]
BUBBLE_RADIUS = 10
BUBBLE_GAP = 30  # Gap between two bubbles
LABEL_GAP = 5
NUMBERING_GAP = 20

# Create a new PDF document
canvas = Canvas("omr_sheet.pdf", pagesize=portrait((PAGE_WIDTH, PAGE_HEIGHT)))

# Draw four sections
for i in range(4):
    # Calculate the position of each section
    section_x = MARGIN_LEFT + i * (SECTION_WIDTH + SECTION_GAP)
    section_y = MARGIN_BOTTOM + 100

    # Draw the section rectangle
    canvas.rect(section_x, section_y, SECTION_WIDTH, SECTION_HEIGHT * 6)

    # Add the question labels
    question_label_x = section_x + 10
    question_label_y = section_y + SECTION_HEIGHT - 20 - NUMBERING_GAP
    canvas.setFont("Helvetica", 12)
    for j in range(5):
        question_label_number = i * 20 + j + 1
        canvas.drawString(question_label_x, question_label_y - j * 45 - NUMBERING_GAP, f"{question_label_number}.")

    # Draw six columns within the section
    for j in range(6):
        # Calculate the position of each column within the section
        column_x = section_x + j * (COLUMN_WIDTH + COLUMN_GAP)
        column_y = section_y

        # Draw the column rectangle
        canvas.rect(column_x, column_y, COLUMN_WIDTH, COLUMN_HEIGHT)

        # Add the question numbers and options
        question_x = column_x + 10
        question_y = column_y + COLUMN_HEIGHT - 20 - NUMBERING_GAP

        for k in range(5):
            question_number = i * 20 + j * 5 + k + 1
            canvas.setFont("Helvetica", 12)
            canvas.drawString(question_x, question_y - k * 45 - NUMBERING_GAP, f"{question_number}.")

            for l, option in enumerate(OPTIONS):
                bubble_x = question_x + 40 + (l * (2 * BUBBLE_RADIUS + BUBBLE_GAP)) + NUMBERING_GAP
                bubble_y = question_y - k * 45 - 30

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
