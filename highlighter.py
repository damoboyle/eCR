from typing import Tuple
from io import BytesIO
import os
import re
import fitz

# Search for terms within the document lines
def search_for_text(lines, search_str):
    for line in lines:
        results = re.findall(search_str, line, re.IGNORECASE)   # Find all matches within one line
        
        # In case multiple matches within one line
        for result in results:
            yield result

# Highlight matching values
def highlight_matching_data(page, matched_values):
    matches_found = 0
    
    # Loop throughout matching values
    for val in matched_values:
        matches_found += 1
        matching_val_area = page.search_for(val)
        highlight = None
        highlight = page.add_highlight_annot(matching_val_area)
        """
        # To change the highlight color
        highlight.setColors({"stroke":(0,0,1),"fill":(0.75,0.8,0.95) })
        highlight.setColors(stroke = fitz.utils.getColor('white'), fill = fitz.utils.getColor('red'))
        highlight.setColors(colors= fitz.utils.getColor('red'))
        """
        highlight.update()
        
    return matches_found

# Process the pages of the PDF File
def process_data(input_file: str, output_file: str, search_str: str, pages: Tuple = None):
    pdfDoc = fitz.open(input_file)      # Open the PDF
    output_buffer = BytesIO()           # Save the generated PDF to memory buffer
    total_matches = 0
    
    ###ADD FOR LOOP AND PASS LIST OF TERMS HERE FOR MORE EFFICIENT PROCESSING###
    # Iterate through pages
    for pg in range(pdfDoc.page_count):
    
        # If required for specific pages
        if pages:
            if str(pg) not in pages:
                continue
        
        page = pdfDoc[pg]                                           # Select the page
        page_lines = page.get_text("text").split('\n')              # Split page by lines
        matched_values = search_for_text(page_lines, search_str)    # Get Matching Data
        
        if matched_values:
            matches_found = highlight_matching_data(page, matched_values)
            total_matches += matches_found
            
    #print(f"{total_matches} Match(es) Found of Search String {search_str} In Input File: {input_file}")
    
    # Save to output
    pdfDoc.save(output_buffer)
    pdfDoc.close()
    
    # Save the output buffer to the output file
    with open(output_file, mode = 'wb') as f:
        f.write(output_buffer.getbuffer())
    f.close()
    
    #Added for if statements used in routing from review.py
    return total_matches


#Code modified from:
#https://www.thepythoncode.com/article/redact-and-highlight-text-in-pdf-with-python