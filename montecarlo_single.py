import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import datetime

file = pd.read_csv("Bitstamp_BTCUSD_d.csv", parse_dates=True)
date = pd.to_datetime(file.date)
data = file.close
#plt.plot(date, data)
#plt.show()

filex = pd.read_csv("Bitstamp_BTCUSD_f.csv", parse_dates=True)
datex = pd.to_datetime(filex.date)
datax = filex.close

log_returns = np.log(1 + datax.pct_change())
u = log_returns.mean()
var = log_returns.var()
drift = u - (0.5*var)

stdev = log_returns.std()
days = 1095 # 6 month prediction
iterations = 1
Z = norm.ppf(np.random.rand(days, iterations))
daily_returns = np.exp(drift + stdev * Z)

price_paths = np.zeros_like(daily_returns)
price_paths[0] = datax.iloc[0]
for t in range(1, days):
    price_paths[t] = price_paths[t-1]*daily_returns[t]

base = date.iloc[0]
future_dates = [base + datetime.timedelta(days=x) for x in range(days)]

smalist=[]
c=[]
d=[]
#j = btc_price_list
theta = []
i = 0
d2 = []
zoo=[]
date2 = date[::-1]
data2 = data[::-1]
data3 = data2
#date3 = date2 + future_dates[::-1]
kzm=[]
print(price_paths)
for y in price_paths:
        print(y)
        kzm.append(y)

dt3 = list(date2)
date3 = dt3 + list(future_dates)
d4 = list(data3)
d5 = d4 + list(kzm)
print(len(d4))
print(len(kzm))

print(len(d5))
for x in d5:
    i+=1
    #price = x.close
    #date = x.date
    price = x
    theta.append(price)
    if i>1450:
        del theta[0]
        sma = sum(theta)/1450
        smalist.append(sma)
    else:
        sma = sum(theta)/i
        smalist.append(sma)
        pass
    zoo.append([x, sma])
        #d2.append(date[i-1])
    c.append(price)




plt.plot(date3, smalist, linestyle="dashed", label="sma4")
plt.plot(date, data, linestyle='dashed')
plt.plot(future_dates, price_paths)
plt.ylabel("Close price (BTC/USDT)")
plt.show()



sns.histplot(price_paths[-1,:], bins = 10, stat = "frequency")
plt.xlabel("Close price (BTC/USDT)")
plt.ylabel("Frequency")
plt.show()
