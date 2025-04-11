import numpy as np
import pandas as pd

Employee=['e1','e2','e3','e4','e5']
days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

sales = np.random.randint(0,11,size=(5,7))
df = pd.DataFrame(sales,columns=days,index=Employee)

df['Total'] = df.sum(axis=1)

df['Average'] = df[days].mean(axis=1)

def perfomance(_perfomance):
    if _perfomance >= 50:
        return 'Excellent'
    elif _perfomance >= 30 and _perfomance <= 49:
        return 'Good'
    else:
        return 'Poor'
    
df['Perfomance'] = df['Total'].apply(perfomance)

excellent_df = df[df['Perfomance'] == 'Excellent']
print(df)
print('\n',excellent_df)