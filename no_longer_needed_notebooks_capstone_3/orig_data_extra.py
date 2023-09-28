

columns = ['dhoti_pants', 'saree', 'sherwanis', 'palazzos', 'nehru_jackets', 'petticoats',
           'blouse','dupattas', 'gowns', 'lehenga', 'women_kurta', 'kurta_men', 
           'mojaris_men', 'mojaris_women', 'leggings_and_salwars']


for column in columns:
    dfvr.loc[dfvr['class_label'].eq(dfvr[str(column)]), str(column)] = 1   
   
dfvr.head()
dfvr.loc[1]
dfvr.loc[7499]


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
    

dfvr.head()
dfvr.to_csv('/Users/butler/Documents/springboard_bootcamp/Classification_of_Indian_clothing_images/data/interim/dfvr1.csv')
for i in range(len(saree)):
    if dfvr.iloc[saree[i], 5] == 'saree':
        if dfvr.iloc[saree[i], 23] == 'saree':
            dfvr.iloc[saree[i], 23] = None
for i in range(len(sherwani)):
    if dfvr.iloc[sherwani[i], 5] == 'sherwani':
        if dfvr.iloc[saree[i], 23] == 'sherwani':
            dfvr.iloc[saree[i], 23] = None
dfvr.head()
leggings_and_salwars
dfvr.to_csv('/Users/butler/Documents/springboard_bootcamp/Classification_of_Indian_clothing_images/data/interim/dfvr.csv')

columns = ['kurta', 'women', ' men', 'dhoti', 'saree', 'sherwani', 'palazzo', 
           'mojari', 'nehru', 'legging', 'salwar', 'petticoat', 'blouse', 
           'dupatta', 'gown','lehenga','kurta_men', ]
columns[0]
def func(x):
    if x == True:
        return str(column)
    else:
        return 0
for column in columns:    
    dfvr[str(column)] = dfvr[str(column)].apply(lambda x: func(x))
dfvr.loc[1000]
dfvr.to_csv('/Users/butler/Documents/springboard_bootcamp/Classification_of_Indian_clothing_images/data/interim/dfvr.csv')
dfvr.head()
columns[0]


for column in columns:
    column = dfvr.index[dfvr[str(column)] == True]
    print(column)
df = pd.read_csv('/Users/butler/Documents/hp/Classification_of_Indian_clothing_images/data/interim/dfvr.csv')
df.tail()
df.join(pd.Series(d,name='c'), on=['a','b'])
columns = ['kurta', 'dhoti', 'saree', 'sherwani', 
           'palazzo', 'mojari', 'nehru', 'legging', 'salwar', 
           'petticoat', 'blouse', 'dupatta', 'gown', 'lehenga']


for name in columns:
    if dfvr[str(name)] == str(name):
        dfvr['other_label'] == str(name)
    
       

def func(x):
    for column in columns:
        try:
            if x == column:
                return str(column)
        except:
            print('')
dfvr['other_label'] = dfvr[str(name)].apply(lambda x: func(x))  
dfvr.head()
# Setting df_non_dhoti to df_val_revised with boolean value if 'dhoti' is not in any column
df_non_dhoti = df_val.applymap(lambda x: 'dhoti' not in str(x).lower())
dfvr.tail()
dfvr.other_label.nunique()

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
mojari = list(mojari)
dhoti = list(dhoti)
saree = list(saree)
sherwani = list(sherwani)
palazzo = list(palazzo)
nehru = list(nehru)
legging = list(legging)
salwar = list(salwar)
petticoat = list(petticoat)
blouse = list(blouse)
dupatta = list(dupatta)
gown = list(gown)
lehenga = list(lehenga)
women = list(women)
men = list(men)
kurta = list(kurta)

dfk.head()
dfm.head()