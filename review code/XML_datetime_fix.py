#This script was used to fix a known datetime error from a high quantity reporter to allow for hours of reduced work load involved in system configuration
import os
import pathlib
from xml.etree import ElementTree

live_dir = "C:/EMSA/eCR/Processing/"

files = os.listdir(live_dir)                                    #Get list of all XML files in folder

for file in files:                                              #Find Facility ID from filename
    print(file)
    xml_name = pathlib.Path(live_dir + file).stem
    xml_id = xml_name.split('~')[8]
    if '.' in xml_id:
        orgID = xml_id.split('.')[6]
    else:
        orgID = xml_id.split('_')[0]
        
    if orgID == "188":                                          #Separate *Specific Facility* Files for Editing
        tree = ElementTree.parse(live_dir + file)               #Parse File
        branches = tree.findall('.//{*}organizer')              #Get Branch(es) with Lab Data
        for branch in branches:
            collection_time = branch.find('.//{*}component/{*}procedure/{*}effectiveTime')
            if collection_time != None:                         #Handle missing <organizer> tag
                try:                                            #Catch situations where effectiveTime is a <low><high> range
                    for test_date in branch.findall('.//{*}component/{*}observation/{*}effectiveTime'):
                        if len(test_date.attrib['value']) < 9:  #Select only values that are improperly coded/reported
                            test_date.set('value', collection_time.attrib['value'])
                except KeyError:
                    continue
                        
                #Write updates to XML file
                tree.write(live_dir + file, encoding="utf-8", xml_declaration=True)