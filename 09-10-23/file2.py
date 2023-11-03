import numpy as np
import pandas as pd
sales_data=np.array([[500, 600, 750, 900],
                    [300, 350, 400, 450],
                    [200, 250, 300, 350]])

price_per_data=np.array([10,15,20,25])

quartely_revenue= np.dot(sales_data,price_per_data)
print(np.sum(quartely_revenue))

for i in range(len(quartely_revenue)):
    print(f"Catgegory {i+1}: ",quartely_revenue[i])

s=pd.Series([1,3,5,np.nan,6,8])
print(s)

dates=pd.date_range("20230101",periods=6)
print(dates)

df=pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
print(df.tail(2))
print(df.columns)
print(df.to_numpy())
print(df.describe())
print(df.dtypes)
print(df.T)
print(df.sort_index(axis=1, ascending=False))
print(df.sort_values(by='B'))
print(df['A'])
print(df[0:3])
print(df['20230103':'20230104'])
print(df.loc[dates[0]])
print(df.loc['20230102':'20230104',['A','B']])
print(df.iloc[3])
print(df[df['A']>0])
df2=df.copy()
df2['E']=['one','one','two','three','four','three']
print(df2)