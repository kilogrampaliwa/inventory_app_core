from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

class InvoicePDFGenerator:
    def __init__(self, filename):
        self.filename = filename

    def create_pdf(self, invoice_data):
        c = canvas.Canvas(self.filename, pagesize=A4)
        page_width, page_height = A4

        # Header (Invoice details)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, page_height - 50, f"Invoice date: {invoice_data['invoice_date']}, Place: {invoice_data['place']}")
        c.drawString(350, page_height - 50, f"Invoice number: {invoice_data['invoice_number']}")
        c.drawString(350, page_height - 65, f"Sale date: {invoice_data['sale_date']}")
        c.drawString(350, page_height - 80, f"Type of payment: {invoice_data['payment_type']}")
        c.drawString(350, page_height - 95, f"Payment deadline: {invoice_data['payment_deadline']}")

        # Seller & Buyer Information
        c.setFont("Helvetica", 10)
        c.drawString(50, page_height - 130, "Salesman:")
        c.drawString(50, page_height - 145, invoice_data['seller']['name'])
        c.drawString(50, page_height - 160, invoice_data['seller']['address1'])
        c.drawString(50, page_height - 175, invoice_data['seller']['address2'])
        c.drawString(50, page_height - 190, f"ID: {invoice_data['seller']['id']}")
        c.drawString(50, page_height - 205, f"Email: {invoice_data['seller']['email']}")

        c.drawString(350, page_height - 130, "Client:")
        c.drawString(350, page_height - 145, invoice_data['buyer']['name'])
        c.drawString(350, page_height - 160, invoice_data['buyer']['address1'])
        c.drawString(350, page_height - 175, invoice_data['buyer']['address2'])
        c.drawString(350, page_height - 190, f"ID: {invoice_data['buyer']['id']}")

        # Table Setup
        table_data = invoice_data['items']
        col_widths = [25, 130, 40, 40, 55, 55, 40, 55, 65]  # Adjusted for A4 width
        table = Table(table_data, colWidths=col_widths)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ]))
        table.wrapOn(c, 50, page_height - 270)
        table.drawOn(c, 30, page_height - 600)  # Adjusted position

        # Summary
        c.drawString(350, page_height - 630, f"Net value: {invoice_data['summary']['net_value']}")
        c.drawString(350, page_height - 645, f"VAT: {invoice_data['summary']['vat']}")
        c.drawString(350, page_height - 660, f"Total: {invoice_data['summary']['total']}")

        # Footer (Signatures & Notices)
        c.drawString(50, 80, "Invoice without client signature")
        c.drawString(350, 80, "Person authorized to issue Invoice")
        c.drawString(350, 65, "(Stamp Place)")

        c.save()
        print(f"PDF saved as {self.filename}")

# Example Usage:
if __name__ == "__main__":
    invoice_data = {
        "invoice_date": "2024-01-22",
        "place": "Warsaw",
        "invoice_number": "INV-2024-001",
        "sale_date": "2024-01-21",
        "payment_type": "Bank Transfer",
        "payment_deadline": "2024-02-05",
        "seller": {
            "name": "Company XYZ",
            "address1": "123 Business St.",
            "address2": "Warsaw, Poland",
            "id": "PL1234567890",
            "email": "contact@companyxyz.com"
        },
        "buyer": {
            "name": "John Doe",
            "address1": "456 Customer Rd.",
            "address2": "Krakow, Poland",
            "id": "PL0987654321"
        },
        "items": [
            ["No.", "Item", "GTU", "Qty", "Net Price", "Total Net", "VAT", "VAT Value", "Total Brutto"],
            ["1", "Muffler", "GTU_07", "1 szt.", "699.19", "699.19", "23%", "160.81", "860.00"],
            ["2", "Spring", "", "50 szt.", "2.03", "101.50", "23%", "23.35", "124.85"]
        ],
        "summary": {
            "net_value": "10898.83",
            "vat": "2506.69",
            "total": "13405.52"
        }
    }

    pdf_generator = InvoicePDFGenerator("invoice.pdf")
    pdf_generator.create_pdf(invoice_data)
