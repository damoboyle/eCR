from datetime import datetime
import csv

def list_em(contents, log):
    current = datetime.now()
    
    with open(log, 'a', newline = '') as file:
        write = csv.writer(file)
        
        for item in contents:
            write.writerow([item, str(current)])
    
    file.close()