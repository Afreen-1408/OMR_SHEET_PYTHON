from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen.canvas import Canvas

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
COLUMN_HEIGHT = (PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM) // 5

# Number of columns
NUM_COLUMNS = 25

# Create a new PDF document
canvas = Canvas("columns.pdf", pagesize=portrait((PAGE_WIDTH, PAGE_HEIGHT)))

# Draw columns
for i in range(NUM_COLUMNS):
    # Calculate the position of each column
    column_x = MARGIN_LEFT + (i % 5) * COLUMN_WIDTH
    column_y = MARGIN_BOTTOM + (i // 5) * COLUMN_HEIGHT

    # Draw the column rectangle
    canvas.rect(column_x, column_y, COLUMN_WIDTH, COLUMN_HEIGHT)

# Save and close the PDF document
canvas.save()
