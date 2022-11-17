from datetime import date
from jugaad_data.nse import bhavcopy_save
from jugaad_data.holidays import holidays
import pandas as pd
import os,glob
import requests

# Using jugaad_data package to get bhavcopies  


# Setting the path
path=os.path.join('C:',os.sep,"Users","Harsh","Desktop","NseGain","bhavcopies")


# Getting Securities available for Equity segment
res=requests.get("https://archives.nseindia.com/content/equities/EQUITY_L.csv")
content=res.content
csv_file=open(os.path.join(path,"Securities.csv"),"wb")
csv_file.write(content)
csv_file.close()


#Getting Dates of past 30 business days 
dates=pd.bdate_range(start='8/1/2022',end='16/11/2022',holidays=holidays(2022),freq='C')
dates=dates[len(dates)-30:]


#Getting bhavcopies of the above days
for date in dates:
    bhavcopy_save(date,path)


list_files=glob.glob(os.path.join(path,"*bhav.csv"))
final_df=pd.DataFrame()

# Converting all the bhavcopies into one csv file named EOD
for file in list_files:
  df=pd.read_csv(file)
  df.drop(columns=['Unnamed: 13'],inplace=True)  
  df["TIMESTAMP"]=pd.to_datetime(df["TIMESTAMP"],yearfirst=True) #Converting to datetime
  df=df.apply(lambda x: x.str.strip() if x.dtype=="object" else x)  #Stripping spaces
  final_df=final_df.append(df)
final_df.to_csv("EOD.csv",index=False)