import pandas as pd
import itertools
import random

#remove () and [] from string
def remove_char(test_str):
    test_str = str(test_str)
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

#read in csv
df = pd.read_csv ("Data_Lv2_USDA_PackagedMeals.csv")
#generate random numbers for use in subset
num1=random.randint(0,4439)
num2=num1-100
if(num2<0):
    num2=num1+100
#apply remove_char function to random 100 subset of data
df2 = df['ingredients'].apply(remove_char)[num2:num1]

#get combinations
combinations_list = []
for row in df2:
    combinations = list(itertools.combinations(df2, 2))
    combinations_list.append(combinations)

combination_counts = pd.Series(combinations_list).explode().reset_index(drop=True)
#print top combinations
print(f"TOP COMBINATIONS \n{combination_counts.value_counts()[:3]}")
