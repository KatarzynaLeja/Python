import pandas as pd

#Create pd.Series where 'index' contains days of the current month
# and 'data' contains some numbers (temperatures at noon, currency rates, ...).
temp = [i*0.2 + 20 for i in range(1,32)]

s1 = pd.Series(index=range(1,32), data=temp)
print(s1)
