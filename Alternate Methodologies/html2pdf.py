from xhtml2pdf import pisa

def convert(source_html, output_filename):
    # Read HTML from input file
    html_file = open (source_html, 'r')
    data = html_file.read()
    html_file.close()

    # convert HTML to PDF
    result_file = open(output_filename, 'w+b')  #(truncated binary)
    pisa_status = pisa.CreatePDF(data, dest=result_file)
    result_file.close()

    # False on success - True on error
    return pisa_status.err
    
#Code modified from:
#https://xhtml2pdf.readthedocs.io/en/latest/usage.html