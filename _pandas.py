import pandas

# data = {
#     'name':['mohamed','naveen','jai','sibi'],
#     'age':[18,18,19,17]
# }

# dataframe = pandas.DataFrame(data)
# print(dataframe)
# print('\n')

# print(dataframe['name'])
# print('\n')

# print(dataframe[['name','age']])
# print('\n')
# print('Below is driven from datas.csv file')
# print('\n')
# df = pandas.read_csv('datas.csv')
# getdata = df.head() # To print top 5 rows

# print(getdata.iloc[0]) # get data and make it as row
# print('\n')
# print(getdata.loc[0])
# print('\n')
# print(getdata.describe())
# print('\n')
# print(getdata['SCORE'].mean())
# print('\n')
# print(getdata.dropna())
# print('\n')
# print(getdata.fillna('fuck'))

write_data = {
    'Name': ['Ali', 'Ben', 'Chloe'],
    'Math': [80, 90, 70],
    'Science': [85, 95, 75]
}

df = pandas.DataFrame(write_data)
df.to_csv('datas.csv',index=False)
