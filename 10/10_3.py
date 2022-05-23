
import pandas as pd

# Create pd.DataFrame for the periodic table (ten elements).
# Column names are 'Name', 'Symbol', 'Weight'. 'index' starts from 1 for hydrogen.

names = pd.Series(['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon'])
symbols = pd.Series(['H', 'He', 'Li', 'Be', 'Bo', 'C', 'N', 'O', 'F', 'Ne'])
weight = pd.Series([1, 4, 7, 9, 11, 12, 14, 16, 19, 20])

df1 = pd.DataFrame({'Name': names, 'Symbol': symbols, 'Weight': weight})
df1.index = range(1,11)
print(df1)