import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt
dfte = pd.read_json('/Users/butler/Documents/springboard_bootcamp/Classification_of_Indian_clothing_images/data/raw/test_data.json', lines=True)
dfv = pd.read_json('/Users/butler/Documents/springboard_bootcamp/Classification_of_Indian_clothing_images/data/raw/val_data.json', lines=True)
dftr = pd.read_json('/Users/butler/Documents/springboard_bootcamp/Classification_of_Indian_clothing_images/data/raw/train_data.json', lines=True)
#val dhoti 1383 not correct
dfv.head()
dfv.tail()
dfv.class_label.unique()
dfvr = dfv.copy()
dfvr.info()
dfvr = dfvr.reset_index(names='number')
dfvr.tail()
dfvr.tail()
dfvr.head()
dfvr.tail()
columns = ['kurta', 'women', ' men', 'dhoti', 'saree', 'sherwani', 'palazzo', 
           'mojari', 'nehru', 'legging', 'salwar', 'petticoat', 'blouse', 
           'dupatta', 'gown','lehenga']

for column in columns:
    dfvr[str(column)] = dfvr.product_title.str.contains(str(column), flags=re.IGNORECASE)

columns = ['dhoti', 'saree', 'sherwani', 'palazzo', 
           'mojari', 'nehru', 'legging', 'salwar', 'petticoat', 'blouse', 
           'dupatta', 'gown','lehenga']

dhoti = dfvr.index[dfvr['dhoti'] == True]
saree = dfvr.index[dfvr['saree'] == True]
sherwani = dfvr.index[dfvr['sherwani'] == True]
palazzo = dfvr.index[dfvr['palazzo'] == True]
nehru = dfvr.index[dfvr['nehru'] == True]
legging = dfvr.index[dfvr['legging'] == True]
salwar = dfvr.index[dfvr['salwar'] == True]
petticoat = dfvr.index[dfvr['petticoat'] == True]
blouse = dfvr.index[dfvr['blouse'] == True]
dupatta = dfvr.index[dfvr['dupatta'] == True]
gown = dfvr.index[dfvr['gown'] == True]
lehenga = dfvr.index[dfvr['lehenga'] == True]
women = dfvr.index[dfvr['women'] == True]
men = dfvr.index[dfvr[' men'] == True]
kurta = dfvr.index[dfvr['kurta'] == True]
mojari = dfvr.index[dfvr['mojari'] == True]
dfvr['other_label'] = dfvr['women']


for i in range(len(blouse)):
    dfvr.iloc[blouse[i], 23] = 'blouse'

for i in range(len(lehenga)):
    dfvr.iloc[lehenga[i], 23] = 'lehenga'

for i in range(len(dhoti)):
    dfvr.iloc[dhoti[i], 23] = 'dhoti'
columns = ['dhoti', 'saree', 'sherwani', 'palazzo', 
           'mojari', 'nehru', 'legging', 'salwar', 'petticoat', 'blouse', 
           'dupatta', 'gown','lehenga']

for i in range(len(saree)):
    dfvr.iloc[saree[i], 23] = 'saree'

for i in range(len(sherwani)):
    dfvr.iloc[sherwani[i], 23] = 'sherwanis'

for i in range(len(palazzo)):
    dfvr.iloc[palazzo[i], 23] = 'palazzos'

for i in range(len(nehru)):
    dfvr.iloc[nehru[i], 23] = 'nehru_jackets'

for i in range(len(legging)):
    dfvr.iloc[legging[i], 23] = 'legginga_and_salwars'

for i in range(len(salwar)):
    dfvr.iloc[salwar[i], 23] = 'leggings_and_salwars'

for i in range(len(petticoat)):
    dfvr.iloc[petticoat[i], 23] = 'petticoats'

for i in range(len(dupatta)):
    dfvr.iloc[dupatta[i], 23] = 'dupattas'

for i in range(len(gown)):
    dfvr.iloc[lehenga[i], 23] = 'gown'
for i in range(len(kurta)):
    if kurta[i] in women:
        dfvr.iloc[kurta[i], 23] = 'women_kurta'
    if kurta[i] in men:
        dfvr.iloc[kurta[i], 23] = 'kurta_men'
print(dfvr.head())  
print(saree)
for i in range(len(saree)):
    if dfvr.iloc[saree[i], 5] == 'saree':
        if dfvr.iloc[saree[i], 23] == 'saree':
            dfvr.iloc[saree[i], 23] = None
dfvr.to_csv('/Users/butler/Documents/springboard_bootcamp/Classification_of_Indian_clothing_images/data/interim/dfvr1.csv')