#Import Packages
import pandas as pd 
import re
from collections import Counter 
# Read in cleaned dataset
df = pd.read_csv ("Data_Lv2_USDA_PackagedMeals.csv")

#Create Ingredients variable from dataset
ingredients=df["ingredients"]

#Append list with each item in ingredients
myList=[]
for item in ingredients:
    item= str(item)
    myList.append(item)
#cast to str so can use in function
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

#Remove () and []
ingredient_listStr = remove_char(myListStr)
#Remove *
ingredient_listStr_final=ingredient_listStr.replace("*","")

# split() returns list of all the words in the string
split_it = ingredient_listStr_final.split(",")
#print(split_it)
#words_to_count = (word for word in split_it)
#c = Counter(words_to_count)
#print (f"Most common ingredients and how many times occur: {c.most_common(10)}")

ingredient_count = pd.Series(split_it).value_counts()
# Most common ingredients
print(ingredient_count[:10])



   



