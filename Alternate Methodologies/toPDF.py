from xhtml2pdf import pisa             # import python module

# Define your data
source_html = "C:/test1.html"
output_filename = "C:/html1.pdf"

# Utility function
def convert_html_to_pdf(source_html, output_filename):
    ##open input file for reading
    html_file = open(source_html, 'r')
    data = html_file.read()
    html_file.close()

    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            data,                # the HTML to convert
            dest=result_file)           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err

# Main program
if __name__ == "__main__":
    pisa.showLogging()
    convert_html_to_pdf(source_html, output_filename)