import PyPDF2 as PDF
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def read_pdf(pdf_file):
    with open(pdf_file, "rb") as f:
        pdf_reader = PDF.PdfReader(f)
        print(len(pdf_reader.pages))
        print(pdf_reader.pages[0].extract_text())

def write_pdf(pdf_file, content):
    c = canvas.Canvas(pdf_file, pagesize=A4)
    width, height = A4
    c.drawString(100, height-100, content)
    c.save()

def merge_pdf(output_file, *pdf_files):
    pdf_merger = PDF.PdfWriter()

    for pdf_file in pdf_files:
        with(open(pdf_file, "rb")) as f:
            pdf_merger.append(f)

    with open(output_file, "wb") as f:
        pdf_merger.write(f)

def split_pdf(pdf_file):
    with open(pdf_file, "rb") as f:
        pdf_reader = PDF.PdfReader(f)

        i=0
        for page in pdf_reader.pages:
            pdf_writer = PDF.PdfWriter()
            pdf_writer.add_page(page)

            with open(f"output{i}.pdf", "wb") as f:
                pdf_writer.write(f)

            i+=1

def main():
    #read_pdf("test.pdf")
    write_pdf("test_w.pdf", "Hello World")
    #merge_pdf("merge.pdf", "test_w.pdf", "test.pdf")
    #split_pdf("merge.pdf")

if __name__ == '__main__':
    main()