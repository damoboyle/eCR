import os
import pathlib
import shutil

import pyppdf

import log

def log_convert_move(dir, move, save, log_file):
    #Get list of all files in location
    files = os.listdir(dir)
    
    #Record file names and datetime in log
    log.list_em(files, log_file)
    
    #Iterate through and covert available files
    for file in files:
        filename = pathlib.Path(dir + file).stem                    #Get filename without extension
        pyppdf.save_pdf(save + filename + '.pdf', dir + file)       #(output, input)
        
        #Move HTML files that have already been converted to the folder of original HTML files
        shutil.move(dir + file, move + file)
        
    
    ##Can be used to ignore folders if there are folders in the path location##
    """
    dir_path = "I:/eCR/"
    
    res = []
        
    for path in os.listdir(dir_path):
    # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    """