from xml.dom import minidom
import pathlib
import shutil
import os

def report(dir, pdf, move, pending):
    #Get list of all RR files in folder
    files = os.listdir(dir)
    
    for file in files:
        xml = minidom.parse(dir + file)
        
        values = xml.getElementsByTagName('value')

        for rson in values:
            if (rson.attributes['xsi:type'].value == 'ST'):
                if(rson.firstChild.data = 'COVID-19 (as a diagnosis or active problem)'):
                    #Identify matching eCR file
                    ##FILES ARE TIMESTAMPED, REMOVE TIMESTAMP TO ENSURE INTEROPERABILITY##
                    filename = pathlib.Path(dir + file).stem
                    filename = filename.replace('~RR', '~eICRHTML')
                    filename = filename.replace('_RR', '_eICR')
                    
                    #Move eCR PDF to covid folder
                    shutil.move(pdf + filename + '.pdf', move)
                    
                else:
                    shutil.move(pdf + filename + '.pdf', pending)