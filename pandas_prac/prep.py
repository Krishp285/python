import pandas as pd
import numpy as np
"""
df = pd.read_csv("pandas_prac\mckinsey.csv")
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())
print(df.isnull().sum())  # check  null value for  count  
print(df.size)
print(df.values)
print(df.keys())
"""

# dataframe create manually :  add , rename , drop  

"""df =pd.DataFrame([
    ["priyanshi",10000,25],
    ["krish",20000,22],
    ["krishna",30000,23],
    ["dev",40000,14]
],columns=["name","salary","age"])

print(df)
print(df.rename(columns={"name":"first_name"}))
"""

"""df1=pd.DataFrame({
    "name" : ["priyanshi","krish","krishna","dev"],
    "salary" : [10000,20000,30000,40000],
    "age" : [25,22,23,14]
})
print(df1)

df1["gender"]=['f','m','f','m']
df1 = df1.rename(columns={"name":"first_name"})
df1.rename(columns={"name":"first_name"},inplace=True)

df1.drop(columns=["age"],inplace=True)
print(df1)
"""

# read csv : 

"""
df = pd.read_csv("pandas\mckinsey.csv")

print(df)
df=df['year']
df = df[["year","continent"]]
df["next_survey_year"] = df["year"] +3 

df = df["country"].unique()
df = df['country'].nunique()
df =df['country'].value_counts()
df['GDP'] =df["gdp_cap"] * df['population']

df['new_index']=np.arange(5,1709)
df.index= np.arange(1,1705)
print(df.head())
"""

# implicit index  vs explicit index :
"""
implicit  index : always start with 0 . 

explicit index : we can define it as we want (what is seen in output of a dataframe). 
it can be string , float whatever we want. 

"""

df = pd.read_csv("pandas\mckinsey.csv")

"""print(df.head(20))
print(df['country'][16])
print(df['country'][17])

"""
# pandas give  two method : 
"""
1. loc : explict index
2. iloc : implicit index
"""
# print(df.loc[1])
# print(df.iloc[1])

# print(df.loc[5 :13])
# print(df.iloc[5 :13])  # last  value  excluded 

# print(df.iloc[2 :5,1:4])
# print(df.loc[2 :5,"year" :"continent"])

# print(df.loc[2 :5,["country","year","continent"]])

# print(df.iloc[[1,4,6,7],[0,3,4]])

# print(df.iloc[-1])
# print(df.loc[-1])

"""
que : give me year =2002 
"""

# print(df.loc[df['year']==2002])  # give  output  year =2002 
# print(df.iloc[df['year']==2002])  # error 

"""
df = df.drop([2,3,6,8]).head(20)
print(df)
"""