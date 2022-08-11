import os
import openpyxl
import pandas as pd
from itertools import islice

#Reading a directory of folders 

mypath = r""
#yourpath = os.getcwd()
fpath = r''

#empty_df = pd.DataFrame()
for root, dirs, files in os.walk(mypath, topdown=False):
    for name in files:
        file = (os.path.join(root, name))
        #print(file)
        
        #df1 = pd.read_excel(file, sheet_name='Schedule')
        #print(df1)
        
        #append each file into the original empty dataframe
        #df = df.append(df1)
        #print(df)
        
        #transfer final output to an Excel (xlsx) file on the output path 
        #df.to_excel(fpath)
        
        wb = openpyxl.load_workbook(file)
        sh = wb['Schedule']
        data = sh.values
        #print(data)
        cols = next(data)[1:]
        #print(cols)
        data = list(data)
        #print(data)
        idx = [r[0] for r in data]
        #print(idx)
        data = (islice(r, 1, None) for r in data)
        #print(data)
        df = pd.DataFrame(data, index=idx, columns=cols)
        #print(df)
        #df.to_excel(fpath)
        
        
        with pd.ExcelWriter(r'',mode='a',engine="openpyxl", if_sheet_exists='overlay') as writer:  
            df.to_excel(writer, sheet_name='Sheet1', engine="openpyxl")
        
        
        
        '''
        #writing results from above to a single file 
        filename = r""
        outputfile = r""
        #pd.ExcelFile(filename).sheet_names
        writer = pd.ExcelWriter(outputfile, engine="xlsxwriter")
        CombinedData = pd.DataFrame()
        for sht in pd.ExcelFile(filename).sheet_names:
            df = pd.read_excel(filename, sheet_name = sht)
            CombinedData = CombinedData.append(df)
            CombinedData.to_excel(writer, sheet_name = "AllData", index = False)
            writer.save()
        '''
        
        #def append_to_excel(fpath, df):
            #with pd.ExcelWriter(fpath, mode="a", if_sheet_exists = 'overlay') as f:
                #df.to_excel(f, sheet_name=sheet_name)

        #append_to_excel(fpath, df)
        
        
        #print(sh.cell(12,11).value)
        #for i in df.index:
            #try:
                #export = df.loc[i]
                #print(export)
                
            #except:
                #print("error")
