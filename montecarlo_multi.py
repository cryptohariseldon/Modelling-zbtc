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
fsma = []
iter2 = 1000
for o in range(0,iter2):
    log_returns = np.log(1 + datax.pct_change())
    u = log_returns.mean()
    var = log_returns.var()
    drift = u - (0.5*var)

    stdev = log_returns.std()
    days = 730 # Set time period here
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
    #print(price_paths)
    for y in price_paths:
            #print(y)
            kzm.append(y)
    kmax = len(kzm)
    dt3 = list(date2)
    date3 = dt3 + list(future_dates)
    d4 = list(data3)
    d5 = d4 + list(kzm)
    #print(len(d4))
    #print(len(kzm))
    dist = len(d4)
    final = len(d5)
    #print(len(d5))
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


    final_sma = smalist[final-1]
    fsma.append(final_sma)
    print(final_sma)
    final_price = kzm[kmax-1]
    #print("fp=")
    #print(final_price)

initial_sma = smalist[dist-1]
print(initial_sma)

p25 = []
fiftyup = 0
fortyup = 0
thirtyup = 0
twentyup=0
tenup=0
zeroup=0
zerodown=0
tendown=0
twentydown=0
thirtydown=0
fortydown=0
fiftydown =0
for zep in fsma:
    initial_sma2 = smalist[dist-1]
    pcent_change = (zep-initial_sma2)*100/initial_sma2
    print(pcent_change)
    p25.append(pcent_change)
    if pcent_change > 50:
        fiftyup +=1
    if pcent_change > 40 and pcent_change <50:
        fortyup += 1
    elif pcent_change >30 and pcent_change < 40:
        thirtyup+=1
    elif pcent_change>20 and pcent_change <30:
        twentyup+=1
    elif pcent_change >10 and pcent_change <20:
         tenup+=1
    elif pcent_change >0 and pcent_change <10:
        zeroup+=1
    elif pcent_change >0 and pcent_change <-10:
        zerodown+=1
    elif pcent_change <-10 and pcent_change >-20:
        tendown+=0
    elif pcent_change <-20 and pcent_change >-30:
        twentydown+=1
    elif pcent_change <-30 and pcent_change >-40:
        thirtydown+=1
    elif pcent_change <-40 and pcent_change >-50:
        fortydown+=1
    elif pcent_change <-50:
        fiftydown+=1

mp50 = fiftydown*100/iter2
mp40 = fortydown*100/iter2
mp30 = thirtydown*100/iter2
mp20 = twentydown*100/iter2
mp10 = tendown*100/iter2
mp0 = zerodown*100/iter2
p0 = zeroup*100/iter2
p10 = tenup*100/iter2
p20 = twentyup*100/iter2
p30 = thirtyup*100/iter2
p40 = fortyup*100/iter2
p50 = fiftyup*100/iter2


from prettytable import PrettyTable

print("projected change in SMA")
print("frequencies:")
fiftyup, fortyup
print("likelyhood:")
print("less than -40%:" + str(mp40), "-30% to -40%"+str(mp30), "-20% to -30%")
print(mp40, mp30, mp20, mp10, mp0, p0, p10, p20, p30, p40)


myTable = PrettyTable(["Range", "Frequency", "Likelyhood"])
#myTable.add_row(["less than -40%:", str(fortydown), str(mp40)])

myTable.add_row(["Less than -50%", fiftydown, mp50])
myTable.add_row(["-40% to -50%", fortydown, mp40])
myTable.add_row(["-30% to -40%", thirtydown, mp30])
myTable.add_row(["-20 to -30", twentydown, mp20])
myTable.add_row(["-10 to -20", tendown, mp10])
myTable.add_row(["0 to -10", zerodown, mp0])
myTable.add_row(["0 to 10", zeroup, p0])
myTable.add_row(["10 to 20", tenup, p10])
myTable.add_row(["20 to 30", twentyup, p20])
myTable.add_row(["30 to 40", thirtyup, p30])
myTable.add_row(["40 to 50", fortyup, p40])
myTable.add_row(["above 50", fiftyup, p50])



print(myTable)




"""
plt.plot(date3, smalist, linestyle="dashed", label="sma4")
plt.plot(date, data, linestyle='dashed')
plt.plot(future_dates, price_paths)
plt.ylabel("Close price (BTC/USDT)")
plt.show()
"""

"""
sns.histplot(p, bins = 10, stat = "frequency")
plt.xlabel("Close price (BTC/USDT)")
plt.ylabel("Frequency")
plt.show()"""
