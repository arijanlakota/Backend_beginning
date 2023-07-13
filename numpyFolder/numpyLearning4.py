from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
#poissonDistribution
# arr = random.poisson(lam = 2,size = 100)
# sns.displot(arr)
# plt.show()
# arr1 = random.normal(loc=50,scale=7,size=1000)
# arr2 = random.poisson(lam=50,size=1000)
# sns.displot(arr1,kind="kde",label="normal")
# sns.displot(arr2,kind="kde",label="poisson")
# plt.show()
# sns.displot(random.binomial(n = 2000,p =0.02,size=1000),kind="kde",label="binomial")
# sns.displot(random.poisson(lam=10,size=1000),kind="kde",label="poisson")
# plt.show()
#unifromDistribution
# x = random.uniform(size=(3,4))
# print(x)
# arr = random.uniform(size=1000)
# sns.displot(arr,kind="kde")
# plt.show()
#logisticDistribution
# x = random.logistic(size=1000,loc=1,scale=2)
# sns.displot(x,kind="kde")
# plt.show()
#multinomialDitribution
# x = random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
# print(x)
#exponentialDistribution
# x = random.exponential(scale=2,size=100)
# sns.displot(x,kind="kde")
# plt.show()
#chiSquareDisrtibution
# x = random.chisquare(df=2,size=1000)
# sns.displot(x,kind="kde")
# plt.show()
# x = random.rayleigh(scale=2,size=1000)
# sns.displot(x,kind="kde")
# plt.show()
#paretoDistribution
# x = random.pareto(a=2,size=1000)
# sns.displot(x)
# plt.show()
#zipfDistribution
# x = random.zipf(a = 2,size=1000)
# sns.histplot(x[x<10])
# plt.show()
