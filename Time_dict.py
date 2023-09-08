import time
import calendar
import pandas as pd


seq = ('name', 'age', 'sex')
val =("durga prasanna",18,"female")
dic = dict.fromkeys(seq,(12))
print("New Dictionary using from keys :",dic  )

my = {}

for i in range(len(seq)):
    my[seq[i]] = val[i]
print(my)


now = time.time()
print("time:" ,now)
localtime = time.localtime(time.time())
print(localtime)

data = {'Date': ['2023-09-05', '2023-08-15', '2022-07-25', '2022-06-10']}
df = pd.DataFrame(data)
df["dob"] = pd.to_datetime(df['Date'],format = '%Y-%m-%d')

#extracting year month from date
df['year']  = df['dob'].dt.year
df['month'] = df['dob'].dt.month

print(df[['dob','month','year']])

print("normal time readable format:",time.asctime(time.localtime(time.time())))







