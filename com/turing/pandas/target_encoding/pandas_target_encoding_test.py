import pandas as pd

df = pd.DataFrame({
    'x_0': ['a'] * 5 + ['b'] * 5,
    'x_1': ['c'] * 9 + ['d'] * 1,
    'y': [1,1,1,1,0,1,0,0,0,0]
})

means = df.groupby('x_0')['y'].mean()

print(df)
print(means)

#replace each value in x0 with the matching mean
df['x_0'] = df['x_0'].map(means)

print(df)

#do the same for x1
df['x_1'] = df['x_1'].map(df.groupby('x_1')['y'].mean())
print(df)















