import pandas as pd

#list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']

#Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)

print('-------create dataframe from dict-------')
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age':[20,21,19,18]}

#Create DataFrame
df = pd.DataFrame(data)

#Print the output
print(df)



