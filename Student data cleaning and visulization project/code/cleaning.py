#libraries
import pandas as pd
import numpy as np

#read file
data=pd.read_excel("raw_student_data.xlsx")
#drop duplicates
data=data.drop_duplicates()
#clean age column
data["age"]=data["age"].fillna(data["age"].mean())
data["age"]=data["age"].astype(int)
#clean gender column
data["gender"]=data["gender"].str.title()
data["gender"]=data["gender"].str.strip()
data["gender"]=data["gender"].fillna("Unknown")
#clean name column
data["name"]=data["name"].str.strip()
data["name"]=data["name"].str.title()
#clean city column
data["city"]=data["city"].str.title()
data["city"]=data["city"].replace({"Lahor":"Lahore","Karachii":"Karachi"})
data["city"]=data["city"].fillna("Unknown")
#clean grade column
data["grade"]=data["grade"].fillna(data["grade"].mode()[0])
#clean marks column
data.loc[(data["marks"]>100) | (data["marks"]<0),"marks"]=np.nan
data["marks"]=data["marks"].fillna(data["marks"].mean()).astype(int)
#clean fee column
data["fees_paid"]=data["fees_paid"].fillna(data["fees_paid"].mode()[0])
data["fees_paid"]=data["fees_paid"].astype(str).str.title()
data["fees_paid"]=data["fees_paid"].replace({"True":"Yes","False":"No"})
#clean enrollment date column
data["enrollment_date"]=pd.to_datetime(data["enrollment_date"],errors="coerce")
default=pd.to_datetime("2025-10-11")
data["enrollment_date"]=data["enrollment_date"].fillna(default)
data["enrollment_date"]=data["enrollment_date"].dt.strftime("%y-%m-%d")
#clean phone column
data["phone"]=data["phone"].str.replace(r"\D","",regex=True)
data.loc[data["phone"].str.len()!=11,"phone"]=np.nan
data["phone"]=data["phone"].fillna("00000000000")
#finally save cleaned excel file
data.to_excel("Final Cleaned Data.xlsx",index=False)
