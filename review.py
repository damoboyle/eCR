import os
import csv
import shutil

import highlighter

def highlight(dir, conditions, move, pending):
    groups = ['BEE', 'CT and GC', 'General CD', 'Hepatitis', 'HIV', 'Syphilis', 'TB', 'Vectorborne']
    
    #Get list of all files in Processing folder
    files = os.listdir(dir)
    
    for file in files:
        total = 0
    
        for group in groups:
            found = 0
            
            #Opens condition list for each group
            with open (conditions + group + '.csv', 'r', newline = '') as conditionList:
                category = csv.reader(conditionList)
                    
                #Searches for term in condition list and highlights all occurances
                for term in category:
                    found += highlighter.process_data(dir + file, dir + file, term[0])
                    total += found

            conditionList.close()
            
            #Environmental reports have to be routed to a sub-directory
            if group = 'BEE':
                group = 'BEE/Reports/'
            
            #Copies files to designated group folder if matches were found
            if found > 0:
                shutil.copy(dir + file, move)
        
        #Deletes file from Processing folder if matches were found
        #Moves file to Pending folder if no matches were found
        if total > 0:
            os.remove(dir + file)
        else:
            shutil.move(dir + file, pending)