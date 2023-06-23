import time

import converter
import review

if __name__ == '__main__':
    #Directory paths to be passed via definition
    eCR = "H:/eCR/Incoming/"
    html = "H:/eCR/Converted/"
    pdf = "H:/eCR/Processing/"
    log = "H:/eCR/Automation/eCR_log.csv"
    conditions = "H:/eCR/Automation/conditions/"
    move = "G:/Lab Reports/"
    pending = "H:/eCR/Pending/"
    
    converter.log_convert_move(eCR, html, pdf, log)
    time.sleep(2)
    review.highlight(pdf, conditions, move, pending)