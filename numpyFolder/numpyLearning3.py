from numpy import random
import numpy as np
#random
# x = random.randint(100,size=(5))
# print(x)
# x = random.randint(100,size=(3,5))
# print(x)
# y = random.rand(5)
# x = random.choice(y ,size=(3,5))
# print(y)
# print(x)
#random data distribution
# x = random.choice([3,5,7,9] ,p=[0.1,0.3,0.6,0.0] ,size=(100,2)
# print(x)
#Permutations
# x = np.array([1,2,3,4,5,6])
# random.shuffle(x)
# print(x)
# x = np.array([1,2,3,4,5,6])
# print(random.permutation(x))
# print(x)
#seaborn
import matplotlib.pyplot as plt
import seaborn as sns
# sns.displot(np.arange(6) ,kind="kde")
# plt.show()
#normalDistribution
# x = random.normal(size=1000)
# sns.displot(x,kind="kde")
# plt.show()
#binomialDistribution
# x = random.binomial(n = 10,p = 0.5,size=10)
# sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
# sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
# plt.show()