import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')
print(df.head())

# tip learned:

'''
so now, we have many columns so we need to remove the unwanted columns in data

q: how to find the unwanted columns ??

Ans: If the correlation between them is high, then most probably they will be interdependent and hence we can remove one of them

'''
