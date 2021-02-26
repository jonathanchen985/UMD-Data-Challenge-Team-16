import pandas as pd
import matplotlib.pyplot as plt

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
#apply remove_char function
df['ingredients'] = df['ingredients'].apply(remove_char)

#create list for all ingredients
all_ingredients = [] 
for row in df['ingredients']:
    #split each ingredient at comma
    temp = row.split(',')
    #remove leading and trailing whitespace
    temp = list(map(str.strip,temp))
    #remove * and .
    all_ingredients += list(map(lambda _: _.strip('*.'),temp))
#make series    
all_ingredients = pd.Series(map(str.strip,all_ingredients))
#get series of ingredients and their counts
count = all_ingredients.value_counts()
#print top ingredients and their counts
print(f"OVERALL TOP INGREDIENTS \n{count[:10]}")
#plot top ingredients (MAKE SURE TO DOWNLOAD PYTHON EXTENSION PACK IF IN VSC)
count[:10].plot(kind='bar')
plt.show()

