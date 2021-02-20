
import pandas as pd 
import re

df = pd.read_csv ("Data_Lv2_USDA_PackagedMeals.csv")

ingredients=df["ingredients"]
print(ingredients)

myList=[]
for item in df["ingredients"]:
    item= str(item)
    item=item.split(",")
    
   



