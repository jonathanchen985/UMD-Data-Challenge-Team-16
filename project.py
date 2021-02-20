#Import Packages
import pandas as pd 
import re
# Read in cleaned dataset
df = pd.read_csv ("Data_Lv2_USDA_PackagedMeals.csv")

#Create Ingredients variable from dataset
ingredients=df["ingredients"]

#Append list with each item in ingredients
myList=[]
for item in ingredients:
    item= str(item)
    myList.append(item)
myListStr=str(myList)    

#Function: Remove items within parentheses, brackects and curly brackets
def remove_char(test_str):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in test_str:
        if i == '[':
            skip1c += 1
        elif i == '(':
            skip2c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif i == ')'and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret

#Remove '*' in myList 
ingredient_list = remove_char(myListStr)
print(ingredient_list.replace("*",""))


   



