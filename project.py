
import pandas as pd 
import re

df = pd.read_csv ("Data_Lv2_USDA_PackagedMeals.csv")

ingredients=df["ingredients"]
print(ingredients)

myList=[]
for item in df["ingredients"]:
    item= str(item)
    myList.append(item)
myListStr=str(myList)    

def a(test_str):
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

x = "[to promote color retention], (dextrose), turkey sausage link (turkey, mechanically separated turkey, salt, natural flavorings, citric acid), water, seasoning blend (dextrose, corn syrup solids, spices, sugar, bha, bht, citric acid), soy protein concentrate. contains: wheat, soy, egg, milk"
x = a(myListStr)
print (x)

   



