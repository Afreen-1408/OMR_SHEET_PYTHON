from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen.canvas import Canvas

# Page dimensions
PAGE_WIDTH = 2480
PAGE_HEIGHT = 3508

# Margins
MARGIN_TOP = 800
MARGIN_BOTTOM = 200
MARGIN_LEFT = 200
MARGIN_RIGHT = 200

# Section dimensions
SECTION_WIDTH = 520
SECTION_HEIGHT = PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM

# Create a new PDF document
canvas = Canvas("omr_sheet.pdf", pagesize=portrait((PAGE_WIDTH, PAGE_HEIGHT)))

# Draw four sections
for i in range(4):
    # Calculate the position of each section
    section_x = MARGIN_LEFT + i * SECTION_WIDTH
    section_y = MARGIN_BOTTOM

    # Draw the section rectangle
    canvas.rect(section_x, section_y, SECTION_WIDTH, SECTION_HEIGHT)

    # Add the question numbers
    question_x = section_x + 10
    question_y = section_y + SECTION_HEIGHT - 20

    for j in range(50):
        question_number = i * 50 + j + 1
        canvas.setFont("Helvetica", 12)
        canvas.drawString(question_x, question_y - j * 45, f"{question_number}.")

# Save and close the PDF document
canvas.save()
