from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class PDFGenerator:
    def __init__(self, filename, font="Helvetica", font_size=12, margins=(72, 72, 72, 72)):
        """
        Initializes the PDFGenerator with basic configurations.

        :param filename: Output PDF file name
        :param font: Font name for the text (default: Helvetica)
        :param font_size: Font size for the text (default: 12)
        :param margins: Margins as a tuple (left, right, top, bottom) in points (default: 72 points or 1 inch each)
        """
        self.filename = filename
        self.font = font
        self.font_size = font_size
        self.margins = margins

    def create_pdf(self, lines):
        """
        Creates a PDF file from the provided list of text lines.

        :param lines: List of strings to write to the PDF
        """
        # Create a canvas for the PDF
        c = canvas.Canvas(self.filename, pagesize=letter)

        # Set the font
        c.setFont(self.font, self.font_size)

        # Get page dimensions and margins
        page_width, page_height = letter
        left_margin, right_margin, top_margin, bottom_margin = self.margins

        # Define starting position for text
        x_position = left_margin
        y_position = page_height - top_margin
        line_height = self.font_size * 1.2  # Line spacing factor

        # Write each line to the PDF
        for line in lines:
            # If the line goes off the bottom margin, create a new page
            if y_position < bottom_margin + line_height:
                c.showPage()
                c.setFont(self.font, self.font_size)
                y_position = page_height - top_margin

            # Draw the current line of text
            c.drawString(x_position, y_position, line)
            y_position -= line_height

        # Save the PDF
        c.save()
        print(f"PDF saved as {self.filename}")

# Example usage:
if __name__ == "__main__":
    text_lines = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt",
        "ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
        "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in",
        "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat",
        "non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    ]

    pdf = PDFGenerator(
        filename="output.pdf",
        font="Times-Roman",
        font_size=14,
        margins=(50, 50, 50, 50)
    )
    pdf.create_pdf(text_lines)
