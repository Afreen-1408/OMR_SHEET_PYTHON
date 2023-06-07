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
SECTION_HEIGHT = 392

# Column dimensions
COLUMN_WIDTH = 520
COLUMN_HEIGHT = 392

# Gap between sections and columns
SECTION_GAP = 20
COLUMN_GAP = 20

# Bubble options
OPTIONS = ["A", "B", "C", "D"]
BUBBLE_RADIUS = 12

# Gap between numbering and label/bubble
NUMBERING_GAP = 20
LABEL_BUBBLE_GAP = 10

# Create a new PDF document
canvas = Canvas("omr_sheet.pdf", pagesize=portrait((PAGE_WIDTH, PAGE_HEIGHT)))

# Draw the four sections below the existing columns
section_x = MARGIN_LEFT
section_y = MARGIN_BOTTOM

for i in range(4):
    # Draw the section rectangle
    canvas.rect(section_x, section_y, SECTION_WIDTH, SECTION_HEIGHT)

    # Draw six columns within the section
    for j in range(6):
        # Calculate the position of each column within the section
        column_x = section_x
        column_y = section_y + (5 - j) * (COLUMN_HEIGHT + COLUMN_GAP)

        # Draw the column rectangle
        canvas.rect(column_x, column_y, COLUMN_WIDTH, COLUMN_HEIGHT)

        # Add the question numbers and options
        question_x = column_x + 10
        question_y = column_y + COLUMN_HEIGHT - 20

        for k in range(5):
            question_number = i * 30 + j * 5 + k + 1
            canvas.setFont("Helvetica", 12)
            canvas.drawString(question_x, question_y - k * 80 - NUMBERING_GAP, f"{question_number}.")

            for l, option in enumerate(OPTIONS):
                bubble_x = question_x + 40 + (l * 100) + NUMBERING_GAP
                bubble_y = question_y - k * 80 - 30

                # Draw the bubble option circle
                canvas.setStrokeColor(colors.black)
                canvas.setFillColor(colors.white)
                bubble_center_x = bubble_x + BUBBLE_RADIUS
                bubble_center_y = bubble_y + BUBBLE_RADIUS
                canvas.circle(bubble_center_x, bubble_center_y, BUBBLE_RADIUS, fill=1, stroke=1)

                # Add the option label
                canvas.setFillColor(colors.black)
                canvas.setFont("Helvetica", 12)
                label_x = bubble_center_x
                label_y = bubble_center_y + BUBBLE_RADIUS + LABEL_BUBBLE_GAP
                canvas.drawCentredString(label_x, label_y, option)

    # Update the section coordinates for the next section
    section_x += SECTION_WIDTH + SECTION_GAP

# Save and close the PDF document
canvas.save()
