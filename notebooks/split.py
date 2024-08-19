from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf_path, start_page, end_page, output_pdf_path):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for page in range(start_page - 1, end_page):  # Adjust for zero-based index
        writer.add_page(reader.pages[page])

    with open(output_pdf_path, 'wb') as output_pdf:
        writer.write(output_pdf)

start = 419
end = 479
ch = 'chapter_11.pdf'
# Example usage
split_pdf('../assets/AnatomyAndPhysiology-LR.pdf',start,end, ch)  # Splits pages 1 to 5 from input.pdf to output.pdf
