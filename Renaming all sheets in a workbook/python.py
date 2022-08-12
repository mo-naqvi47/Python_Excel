import os
import openpyxl
import pandas as pd
from itertools import islice

#Reading a directory of folders 

mypath = r"T:\WKFC\WKFC MASTER\Reports and Automation\AgRisk Rater Data Extraction\MissingAccounts"
#yourpath = os.getcwd()
fpath = r''

file = r"T:\WKFC\WKFC MASTER\Reports and Automation\AgRisk Rater Data Extraction\AgRisk_MissingAccounts - Copy.xlsx"

controlNumber = []
#empty_df = pd.DataFrame()
for root, dirs, files in os.walk(mypath, topdown=False):
    for control in dirs: 
        controlNumber.append(control)
        
length = len(controlNumber)
i = 0
#while i < length:
    #print(controlNumber[i])
    #i = i+1
#print(controlNumber)

wb = openpyxl.load_workbook(file)
for sheet in wb.worksheets:
    sheet.title = controlNumber[i]
    print(sheet.title)
    i = i+1

#DONT FORGET TO SAVE!!
wb.save(file)
