# UMD-Data-Challenge-Team-16

Project Overview

Questions
  1. What are the most popular ingredients in each meal category and for all meals overall? 
  2. What combinations have appeared together most often?
  3. Which are the healthiest meal options in the restricted database?
  4. What supply chain aspects should we focus on concerning the three ingredient categories of artifical, produce, and meat?



  Helpful resources:
  https://stackoverflow.com/questions/14596884/remove-text-between-and


def select_data_category(data, category):
    cat = data[category].unique()
    print('Select from the following categories')
    for idx,value in enumerate(cat):
        print(f'Enter {idx} to select {value}')
    selection = int(input('Selection: '))
    return data[data[category]==cat[selection]]

meals = select_data_category(df,'branded_food_category')
