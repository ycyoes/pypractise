import pandas as pd

'''
Mathematically this is equivalent to:
     u = (n * x + m * w) / (n + m)
where
     u is the mean we’re trying to compute (the one that’s going to replace our categorical values)
     n is the number of values you have
     x is your estimated mean
     m is the “weight” you want to assign to the overall mean
     w is the overall mean
'''
def calc_smooth_mean(df, by, on, m):
    #Compute the global mean
    mean = df[on].mean()

    #Compute the number of values and the mean of each group
    agg = df.groupby(by, as_index=False)[on].agg(['count', 'mean'])
    print('agg-----------\n', agg, '\n----------------')
    counts = agg['count']
    print("counts:||||||||||||\n", counts)
    means = agg['mean']

    #Compute the "smoothed" means
    smooth = (counts * means + m * mean) / (counts + m)

    #Replace each value by the according smoothed mean
    return df[by].map(smooth)

df = pd.DataFrame({
    'x_0': ['a'] * 5 + ['b'] * 5,
    'x_1': ['c'] * 9 + ['d'] * 1,
    'y': [1,1,1,1,0,1,0,0,0,0]
})


df['x_0'] = calc_smooth_mean(df, by='x_0', on='y', m=10)
df['x_1'] = calc_smooth_mean(df, by='x_1', on='y', m=10)

print(df)




