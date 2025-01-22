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
        
        def draw_header():
            c.setFont("Helvetica-Bold", 10)
            c.drawString(50, page_height - 50, f"Invoice date: {invoice_data['invoice_date']}, Place: {invoice_data['place']}")
            c.drawString(350, page_height - 50, f"Invoice number: {invoice_data['invoice_number']}")
            c.drawString(350, page_height - 65, f"Sale date: {invoice_data['sale_date']}")
            c.drawString(350, page_height - 80, f"Type of payment: {invoice_data['payment_type']}")
            c.drawString(350, page_height - 95, f"Payment deadline: {invoice_data['payment_deadline']}")

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

        def draw_footer():
            c.drawString(50, 50, "Invoice without client signature")
            c.drawString(350, 50, "Person authorized to issue Invoice")
            c.drawString(350, 35, "(Stamp Place)")

        def draw_table(table_data, table_y_position, col_widths=None, header_bg_color=colors.Color(red=(41/255), green=(128/255), blue=(185/255)), body_bg_color=colors.Color(red=(220/255), green=(230/255), blue=(242/255))):
            table = Table(table_data, colWidths=col_widths)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), header_bg_color),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('BACKGROUND', (0, 1), (-1, -1), body_bg_color),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ]))
            table.wrapOn(c, 50, table_y_position)
            table.drawOn(c, 30, table_y_position - len(table_data) * 20)

        table_data = invoice_data['items']
        max_rows_per_page = 25
        table_y_position = page_height - 250
        
        table_start_index = 1
        first_page = True
        
        while table_start_index < len(table_data):
            if first_page:
                draw_header()
                first_page = False
            
            table_end_index = min(table_start_index + max_rows_per_page, len(table_data))
            table_chunk = [table_data[0]] + table_data[table_start_index:table_end_index]
            
            draw_table(table_chunk, table_y_position)
            
            summary_y_position = table_y_position - (len(table_chunk) * 20) - 50
            
            if table_end_index == len(table_data):
                summary_data = [
                    ["Description", "Amount"],
                    ["Net value", invoice_data['summary']['net_value']],
                    ["VAT", invoice_data['summary']['vat']],
                    ["Total", invoice_data['summary']['total']]
                ]
                col_widths_summary = [200, 100]
                # Use custom colors for the summary table
                draw_table(summary_data, summary_y_position, col_widths_summary, header_bg_color=colors.Color(red=(144/255), green=(148/255), blue=(151/255)), body_bg_color=colors.Color(red=(240/255), green=(243/255), blue=(244/255)))
                draw_footer()
            
            if table_end_index < len(table_data):
                c.showPage()
                table_y_position = page_height - 50
            
            table_start_index = table_end_index
        
        c.save()
        print(f"PDF saved as {self.filename}")

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
            ["No.", "Item", "GTU", "Qty", "Net Price", "Total Net", "VAT", "VAT Value", "Total Brutto"]
        ] + [[str(i), "Item", "GTU", "1 szt.", "100.00", "100.00", "23%", "23.00", "123.00"] for i in range(1, 15)],
        "summary": {
            "net_value": "10898.83",
            "vat": "2506.69",
            "total": "13405.52"
        }
    }

    pdf_generator = InvoicePDFGenerator("invoice.pdf")
    pdf_generator.create_pdf(invoice_data)
