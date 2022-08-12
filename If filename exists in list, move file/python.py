import shutil
import os
import pandas as pd

scr = r"T:\WKFC\WKFC MASTER\AV\24. AgRisk Coverage\AgRisk Inforce Raters"
dst = r"T:\WKFC\WKFC MASTER\Reports and Automation\AgRisk Rater Data Extraction\MissingAccounts"

files = os.listdir(scr)
controlList = ['396944','366728','366691','366734','424339','366714','424341','406054','366724','366700','400176','412627','366729','378348','395291','391277','366703','387463','395728','390690','411488','366733','393742','379157','406349','396968','387736','366736']

for f in files:
    if f in controlList:
        shutil.move(scr + '\\' + f, dst)
