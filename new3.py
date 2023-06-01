from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen.canvas import Canvas

# Page dimensions
PAGE_WIDTH = 2080
PAGE_HEIGHT = 3508

# Margins
MARGIN_TOP = 500
MARGIN_BOTTOM = 200
MARGIN_LEFT = 200
MARGIN_RIGHT = 200

# Column dimensions
COLUMN_WIDTH = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT
COLUMN_HEIGHT = 500

# Create a new PDF document
canvas = Canvas("omr_sheet.pdf", pagesize=portrait((PAGE_WIDTH, PAGE_HEIGHT)))

# Draw the top section
top_section_x = MARGIN_LEFT
top_section_y = PAGE_HEIGHT - MARGIN_TOP - COLUMN_HEIGHT

# Draw the top section rectangle
canvas.rect(top_section_x, top_section_y, COLUMN_WIDTH, COLUMN_HEIGHT)

canvas.save()
