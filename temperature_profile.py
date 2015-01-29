import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#weather=pd.read_csv('daily_temp.csv')
df=pd.read_csv('daily_temp.csv', na_values=[" "])

print df
#print df['Boston']
#print df['Austin']
#print df['Atlanta']
#print df['Chicago']
#print df['Cleveland']

#df.boxplot(column='Boston')
#plt.show()
#plt.savefig("Boxplot.png")

#plt.figure()
#graph = stats.probplot(df['Boston'], dist="norm", plot=plt)
#plt.show()

df.hist(column='Boston')
plt.show()
plt.savefig("hist_Boston.png")

df.hist(column='Austin')
plt.show()
plt.savefig("hist_Austin.png")

df.hist(column='Atlanta')
plt.show()
plt.savefig("hist_Atlanta.png")

df.hist(column='Chicago')
plt.show()
plt.savefig("hist_Chicago.png")

df.hist(column='Cleveland')
plt.show()
plt.savefig("hist_Cleveland.png")

#Stats output from ".describe" are the mean, stdev, min, low-mid-high binned, and max. The variance is calculated separate.
#print "Boston Dec-Jan", df['Boston'].describe()#mean 36.652000, std 11.096117, min 18.150000, max 59.170000, 25% 29.290000, 50% 36.090000, 75% 47.472500
#print df['Boston'].var()#123.123816552
#print "Austin Dec-Jan", df['Austin'].describe()#mean 53.982000, std 12.726243, min 34.520000, max 76.380000, 25% 42.542500, 50% 53.165000, 75% 64.492500   
#print df['Austin'].var()#161.957264828
#print "Atlanta Dec-Jan", df['Atlanta'].describe(#)mean 51.778667, std 8.400905, min 32.150000, max 63.730000, 25% 46.152500, 50% 52.725000, 75% 58.327500
#print df['Atlanta'].var()#70.5752050575
#print "Chicago Dec-Jan", df['Chicago'].describe()#mean 30.590000, std 13.815686, min 8.380000, max 49.860000, 25% 20.290000, 50% 33.010000, 75% 39.652500
#print df['Chicago'].var()#141.905731034
#print "Cleveland Dec-Jan", df['Cleveland'].describe()#mean 34.049333, std 13.815686, min 13.110000, max 59.200000, 25% 25.425000, 50% 32.450000, 75% 44.547500  
#print df['Cleveland'].var()#190.873178851
