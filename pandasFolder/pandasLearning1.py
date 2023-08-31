import pandas as pd
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# myVar = pd.DataFrame(mydataset)
# print(myVar)
# print(pd.__version__)
# a = [1, 7, 2]
# myVar = pd.Series(a,index=['x','y','z'])
# print(myVar['y'])
#locating DataFrame
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data,index = ["day1", "day2", "day3"])
# print(df.loc[['day1','day2']])
#readin files
# myVar = pd.read_csv('pandasFolder\data.csv')
# print(myVar)
#printing large files
# myVar = pd.read_csv('pandasFolder\data.csv')
# print(myVar.to_string())
# pd.options.display.max_rows = 9999
# myVar = pd.read_csv('pandasFolder\data.csv')
# print(myVar)
#reading JSON
# myVar = pd.read_json('pandasFolder\data.json')
# print(myVar.to_string())
#directly from dictionary
# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }
# df = pd.DataFrame(data,index = ['a','b','c','d','e','f'])
# print(df)
#viewing data
# df = pd.read_csv('pandasFolder\data.csv')
# print(df.head(10))
# df = pd.read_csv('pandasFolder\data.csv')
# print(df.tail())
# df = pd.read_csv('pandasFolder\data.csv')
# print(df.info())
#cleaning data
# df = pd.read_csv('pandasFolder\data.csv')
# print(df.dropna(inplace=True))
# df = pd.read_csv('pandasFolder\data.csv')
# print(df.fillna(130))
# df = pd.read_csv('pandasFolder\data.csv')
# df['Calories'].fillna(130,inplace=True)
# print(df)
#mean,median,mode
# df = pd.read_csv('pandasFolder\data.csv')
# x = df["Calories"].mean()
# df["Calories"].fillna(x,inplace=True)
# print(df)
# df = pd.read_csv('pandasFolder\data.csv')
# x = df["Calories"].mode()[0]
# df["Calories"].fillna(x,inplace=True)
# print(df)
#cleaning wrong format
# df = pd.read_csv('pandasFolder\data.csv')
# df.dropna(subset=['Date'],inplace=True)
# df['Date'] = pd.to_datetime(df['Date'],format='mixed')
# print(df)
# df = pd.read_csv('pandasFolder\data.csv')
# df.loc[7,'Duration'] = 45
# print(df)
#setting boundaries
# df = pd.read_csv('pandasFolder\data.csv')
# for x in df.index:
#     if df.loc[x,'Duration'] > 120:
#         df.loc[x,'Duration'] = 120
# print(df)
#removing wrong Data
# df = pd.read_csv('pandasFolder\data.csv')
# for x in df.index:
#     if df.loc[x,"Duration"] > 120:
#         df.drop(x,inplace=True)
# print(df)
#see if there are duplicates
# df = pd.read_csv('pandasFolder\data.csv')
# print(df.duplicated())
#remove duplicates
df = pd.read_csv('pandasFolder\data.csv')
df.drop_duplicates(inplace=True)
print(df)


