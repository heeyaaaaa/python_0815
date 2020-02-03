import pandas as pd

from pandas import Series, DataFrame

s = Series(data = ["hi", "hello", "bye"],
           index = ["a","b","c"])

print(s)

def say(one="kim", two = "park") :
    print(one)
    print(two)
    
say("kim")

say(two="hwang")

print(s.iloc[-2])

print(s.loc['b'])

print(s.iloc[[0,2]])

print(s.loc["hi":"bye"])

s = Series( data = [100,200,300],
           index =["a","b","c"])

print(s+10)

b = Series( data = [100,10,300],
           index =["a","b","c"])

print(s+b)

cond = s>100
print(cond)

print(s[s>100])

print(s[cond])

print(b[cond])



data = [[100,200,300],
        [400,500,600],
        [700,800,900],
        ]
df = DataFrame(data, index = ["a","b","c"])

print(df)



from pykrx import stock

df = stock.get_market_ohlcv_by_date(
        "20190101","20191230","005490")


cond = df.iloc[:,0] <df.iloc[:,3]

print(len(df[cond]))

print(df)

sum(df.iloc[:,3]-df.iloc[:,0])

df.iloc[:,3].plot()

df.iloc[:,3].min()

df.iloc[:,3].max()



