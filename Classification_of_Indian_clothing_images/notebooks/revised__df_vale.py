import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt

dfvr = pd.read_csv('/Users/butler/Documents/hp/Classification_of_Indian_clothing_images/data/interim/dfvr.csv')
dfvr.drop('Unnamed: 0', axis=1, inplace=True)

columns = ['kurta', 'women', 'men', 'dhoti_pants', 'saree', 'sherwanis', 
           'palazzos', 'mojaris', 'nehru', 'leggings', 'salwars', 
           'petticoats', 'blouse', 'dupattas', 'gowns', 'lehenga']

names = ['dhoti_pant','kurta']
for name in columns:
    print(dfvr.loc[2500])
    def func(x):
            if x == True:
                return str(name)
            else:
                return 0
        
    dfvr[name] = dfvr[name].apply(lambda x: func(x))

print(dfvr.loc[1000])
dfvr.to_csv('/Users/butler/Documents/hp/Classification_of_Indian_clothing_images/data/interim/dfvr.csv')