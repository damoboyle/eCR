#This script can be used to count the number of files received each day within a user specified month
#Remove all non-eICR files in this folder before running this script or it will fail
import os
import pathlib

xml_dir = "C:/eCR/"
#xmls = os.listdir(xml_dir)

res = []
dates = []

print("WARNING: This script will fail if the directory folder has not been cleared of all non-eCR files (folders are okay)")
month = input("Enter the month for your count in the format yyyymm: ")

print("Reading in eCR filenames (This may take a minute or two)")

for path in os.listdir(xml_dir):
    # check if current path is a file
    if os.path.isfile(os.path.join(xml_dir, path)):
        res.append(path)

print("--filenames recorded, running date match--")

for xml in res:
    xml_name = pathlib.Path(xml_dir + xml).stem
    xml_idtime = xml_name.split('~')[8]
    xml_time = xml_idtime.split('_')[1]
    dates.append(xml_time)
    
for datetime in range(int(month+"01"), int(month+"32")):
    found = 0
    for date in dates:
        if str(datetime) in date:
            found += 1
    print(str(datetime) + ' - ' + str(found))
    
print("WARNING: The 31st day will appear but may not exist in the month you have requested")
print("Run Complete")