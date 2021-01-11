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

print('-----dealing with rows and columns---------')
# Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# select two columns
print(df[['Name', 'Qualification', 'Age']])



