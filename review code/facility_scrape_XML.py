#This script was used to collect reporting facilitiy names to reduce manual effort involved in configurung system
from xml.dom import minidom
import os
import csv

#def report(dir, pdf, move, pending):
live_dir = "C:/eCR/
static_dir = "C:/Documents/xmls/"

#Get list of all XML files in folder
files = os.listdir(static_dir)
rows = []
    
print("Files read")
    
for file in files:
    row = []
    xml = minidom.parse(static_dir + file)
    
    org = xml.getElementsByTagName("serviceProviderOrganization")
    for tags in org:
        name = tags.getElementsByTagName("name")[0].firstChild.nodeValue
        row.append(name)
        
    loinc = xml.getElementsByTagName("code")
    for code in loinc:
        if code.getAttribute('codeSystemName') == 'LOINC':
            row.append(code.getAttribute("code"))
    rows.append(row)
    
print("Values found")
   
with open("C:/Users/oboyld/Desktop/EMSA_eCR.csv", 'a', newline = '') as file:
    write = csv.writer(file)
            
    for item in rows:
        write.writerow(item)
        
file.close()

print("Written to csv")