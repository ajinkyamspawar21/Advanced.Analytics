import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

a=np.array([2,5,6,7,10])
b=np.array([30,24,20,17,7])

#variance Covariance MAtrix
np.cov(a,b)


pizza=pd.read_csv("pizza.csv")

pizza['Promote'].cov(pizza['Sales'])


#Variance Covariance Matrix
np.cov(pizza['Promote'],pizza['Sales'])
pizza.cov()


#correlation 

pizza['Promote'].corr(pizza['Sales'])
pizza['Promote'].corr(pizza['Promote'])


#correlation Matrix

pizza.corr()
np.corrcoef(pizza['Promote'])


#Scatter Plot

sns.scatterplot(data=pizza,x='Promote',y='Sales')
plt.show()

################ insure auto ##################

insure= pd.read_csv("Insure_auto.csv")
insure.corr()


sns.heatmap(
    insure.corr(),
    xticklabels=insure.corr().columns,
    yticklabels=insure.corr().columns,
    annot= True)
plt.show()


sns.pairplot(insure)
plt.show

sns.pairplot(insure,diag_kind='kde')
plt.show

############## Iris######################

iris=pd.read_csv("iris.csv")

sns.heatmap(
    iris.corr(),
    xticklabels=iris.corr().columns,
    yticklabels=iris.corr().columns,
    annot= True)
plt.show()

############ Boston #############

boston=pd.read_csv("Boston.csv")

sns.heatmap(
       boston.corr(),
       xticklabels=boston.corr().columns,
       yticklabels=boston.corr().columns,
       annot=False)          
plt.show()


sns.pairplot(boston)
plt.show()









