import pandas as pd
from itertools import combinations
import random 
from collections import Counter
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

#Create another dataframe
df2 = df['ingredients'].apply(remove_char)

#create list for all ingredients
lst2=[]

lst = df2.to_list()
# Clean up data and put into another list
for i in range(len(lst)):
    #split each ingredient at comma
    temp = lst[i].split(',')
    #remove leading and trailing whitespace
    temp = list(map(str.strip,temp))
    #remove * and .
    temp = list(map(lambda _: _.strip('*.'),temp))
    lst2.append(temp)
    lst[i] = ",".join(temp)

#Combination Function
def collect_pairs(lines, token_count):
    pair_counter = Counter()
    for line in lines:
        unique_tokens = sorted(set(line))  # exclude duplicates in same line and sort to ensure one word is always before other
        combos = combinations(unique_tokens, token_count)
        pair_counter += Counter(combos)
    return pair_counter

#Get the combinations of ingredients     
pairs1 = collect_pairs(lst2, 3)
print(pairs1.most_common(10))

#print(f"TOP COMBINATIONS \n{combination_counts.value_counts()[:3]}")
