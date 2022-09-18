import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Wczytanie danych z plikow
data1 = pd.read_excel(r'RD29A_1.xlsx')
data1_ref = pd.read_excel(r'SAND_1.xlsx')
data2 = pd.read_excel(r'RD29A_2.xlsx')
data2_ref = pd.read_excel(r'SAND_2.xlsx')

def choose_columns(x):
    sample = x['Sample Name']
    Ct = x['Ct Mean']
    df = pd.DataFrame(sample, columns=['Sample Name'])
    df['Ct Mean'] = Ct

    return df

def filter_data(dataframe):
    # Usuniecie duplikatow
    df = dataframe.drop_duplicates(subset = ['Sample Name'])
    # Sortowanie
    df = df.sort_values('Sample Name')
    # Usuniecie proby slepej
    df = df.set_index('Sample Name')
    df = df.drop('H2O')
    
    return df

# Wybranie odpowiednich kolumn
df1 = choose_columns(data1)
df1_ref = choose_columns(data1_ref)
df2 = choose_columns(data2)
df2_ref = choose_columns(data2_ref)

# Filtrowanie
df1 = filter_data(df1)
df1_ref = filter_data(df1_ref)
df2 = filter_data(df2)
df2_ref = filter_data(df2_ref)

# Dodanie wynikow dla genu referencyjnego do tabel df1 i df2
df1['Ct Mean Ref'] = df1_ref['Ct Mean']
df2['Ct Mean Ref'] = df2_ref['Ct Mean']

# Obliczenie dCt
df1['dCt'] = df1['Ct Mean'] - df1['Ct Mean Ref']
df2['dCt'] = df2['Ct Mean'] - df2['Ct Mean Ref']

# Pozyskanie informacji z nazw probek
index = df1.index
number = []
con = []
time = []

for sample in index:
    x = sample.split()
    number.append(x[0])
    con.append(x[1])
    time.append(x[2])

# Usuniecie duplikatow
t = []
for i in time:
    if i not in t:
        t.append(i)

# Dodanie kolumn z czasem
df1['Time'] = time
df2['Time'] = time

# Obliczenie ddCt
def calc_ddCt(dataframe):
    ddCt = []

    for index, row in dataframe.iterrows():
        x = row['Time']
        if x == '1':
            y = row['dCt'] - dataframe['dCt'].values[0]
        if x == '3':
            y = row['dCt'] - dataframe['dCt'].values[3]
        if x == '12':
            y = row['dCt'] - dataframe['dCt'].values[6]
        if x == '24':
            y = row['dCt'] - dataframe['dCt'].values[9]
        if x == '48':
            y = row['dCt'] - dataframe['dCt'].values[12]
        ddCt.append(y)
    
    dataframe['ddCt'] = ddCt
    return dataframe

df1 = calc_ddCt(df1)
df2 = calc_ddCt(df2)

# Obliczenie wzglednego poziomu ekspresji (R)
df1['R'] = 2**(-df1['ddCt'])
df2['R'] = 2**(-df2['ddCt'])

# Obliczenie sredniej wartosci R
results = df1[['R']].copy()
results = results.rename(columns={"R":"R1"})
results['R2'] = df2['R']
results['R Mean'] = (results['R1'] + results['R2']) / 2

# Przyporzadkowanie sredniej wartosci R do list z warunkami
results['Con'] = con

DMSO = []
ABA10 = []
ABA50 = []

for index, row in results.iterrows():
    if row['Con'] == 'DMSO':
        DMSO.append(row['R Mean'])
    elif row['Con'] == 'ABA10':
        ABA10.append(row['R Mean'])
    elif row['Con'] == 'ABA50':
        ABA50.append(row['R Mean'])

# Utworzenie wykresu
labels = t

width = 0.23

X = np.arange(len(labels))
fig, ax = plt.subplots()

D = ax.bar(X - 0.24, DMSO, width, label='DMSO', color='#0750e3')

A10 = ax.bar(X, ABA10, width, label='ABA10', color='#147505')

A50 = ax.bar(X + 0.24, ABA50, width, label='ABA50', color='#8637a6')


ax.set_ylabel('Relative RD29A expression', size=18)
ax.set_xlabel('time [h]', size=18)
ax.legend(loc='best', prop={'size': 15})
ax.set_xticks(X)
ax.set_xticklabels(labels)
ax.tick_params(axis='both', labelsize=15)

fig.set_size_inches(12, 7)
fig.tight_layout()
fig.savefig('RD29A.png', dpi=1200, transparent=False)
