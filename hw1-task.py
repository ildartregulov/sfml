#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# (1) Используя параметры read_csv из pandas прочитать файл csv так,
# чтобы данные были разбиты по соответствующим колонкам 
# (а не все слилось в одну)
df = pd.read_csv('/Users/Ildar/Desktop/HW_lesson_01/UCI_Credit_Card.csv') #TODO


# In[3]:


df.head()


# In[4]:


# (2) выведите, что за типы переменных, сколько пропусков,
# для численных значений посчитайте пару статистик (в свободной форме)


# In[5]:


df.info()


# In[6]:


df.describe(include='all')


# In[7]:


df.describe(include='number')


# In[8]:


df.describe(exclude='object')


# In[9]:


# (3) посчитать число женщин с университетским образованием
# SEX (1 = male; 2 = female). 
# EDUCATION (1 = graduate school; 2 = university; 3 = high school; 4 = others). 

df1=df[df['SEX'] == 2].head()
df2=df1[df1['EDUCATION'] == 2].head()
print("Число женщин с университетским образованием: ", len(df2.index), sep="\t")


# In[10]:


# (4) Сгрупировать по "default payment next month" и посчитать медиану для всех показателей начинающихся на BILL_ и PAY_

df[['BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6','PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5','PAY_6','PAY_AMT1','PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6', 'default.payment.next.month']].groupby('default.payment.next.month').median()

# Решил задачу не оптимальным методом
# Почему данная функция в этом случае работает некорректно?
#df1= df.filter(regex=r'^PAY\_' , axis=1) + df.filter(regex=r'^BILL\_', axis=1) + df.filter(regex='default.payment.next.month' , axis=1)
#df1.head().groupby('default.payment.next.month').median()





# In[11]:


# (5) постройте сводную таблицу (pivot table) по SEX, EDUCATION, MARRIAGE


print (df.pivot_table('SEX', 'EDUCATION', 'MARRIAGE', 'count'))


# In[12]:


# (6) Создать новый строковый столбец в data frame-е, который:
# принимает значение A, если значение LIMIT_BAL <=10000
# принимает значение B, если значение LIMIT_BAL <=100000 и >10000
# принимает значение C, если значение LIMIT_BAL <=200000 и >100000
# принимает значение D, если значение LIMIT_BAL <=400000 и >200000
# принимает значение E, если значение LIMIT_BAL <=700000 и >400000
# принимает значение F, если значение LIMIT_BAL >700000

#TODO
def newfunc(s):
    if (s <=10000): return 'A'
    elif (s <=100000) &  (s >10000): return 'B'
    elif (s <=200000) & (s >100000): return 'C'
    elif (s <=400000) & (s >200000): return 'D'
    elif (s <=700000) & (s >400000): return 'E'
    elif (s >700000): return 'F'
df['LIMIT_BAL'].map(newfunc)


# In[13]:


# (7) постироить распределение LIMIT_BAL (гистрограмму)

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
sns.factorplot('LIMIT_BAL',data=df,kind='count',size=30);


# In[14]:


# (8) построить среднее значение кредитного лимита для каждого вида образования 
# и для каждого пола
# график необходимо сделать очень широким (на весь экран)
#df #TODO

_, ax = plt.subplots(figsize=(50,15))
sns.factorplot('LIMIT_BAL','EDUCATION',data=df,hue='SEX',ax=ax)
plt.legend()
plt.show()
               


# In[15]:


# (9) построить зависимость кредитного лимита и образования только для одного из полов

#TODO
sns.factorplot('LIMIT_BAL','EDUCATION',data=df[df['SEX'] == 1],hue='SEX', size=20);


# In[16]:


# (10) построить большой график (подсказка - используя seaborn) для построения завимисости всех возможных пар параметров
# разным цветом выделить разные значение "default payment next month"
# (но так как столбцов много - картинка может получиться "монструозной")
# (поэкспериментируйте над тем как построить подобное сравнение параметров)
# (подсказка - ответ может состоять из несколькольких графиков)
# (если не выйдет - программа минимум - построить один график со всеми параметрами)
import seaborn
sns.pairplot(df, hue='SEX');

#TODO


# In[24]:


_, axes = plt.subplots(3, 4, sharey=True, figsize=(15,12))
sns.violinplot('LIMIT_BAL', 'SEX', data=df[df['default.payment.next.month']==0], ax=axes[0, 0]);
sns.violinplot('LIMIT_BAL', 'SEX', data=df[df['default.payment.next.month']==1], ax=axes[0, 1]);
sns.violinplot('LIMIT_BAL', 'EDUCATION', data=df[df['default.payment.next.month']==1], ax=axes[0, 2]);
sns.violinplot('LIMIT_BAL', 'EDUCATION', data=df[df['default.payment.next.month']==1], ax=axes[0, 3]);
sns.violinplot('LIMIT_BAL', 'MARRIAGE', data=df[df['default.payment.next.month']==0], ax=axes[1, 0]);
sns.violinplot('LIMIT_BAL', 'MARRIAGE', data=df[df['default.payment.next.month']==1], ax=axes[1, 1]);
sns.violinplot('SEX', 'EDUCATION', data=df[df['default.payment.next.month']==0], ax=axes[1, 2]);
sns.violinplot('SEX', 'EDUCATION', data=df[df['default.payment.next.month']==1], ax=axes[1, 3]);
sns.violinplot('SEX', 'EDUCATION', data=df[df['default.payment.next.month']==0], ax=axes[2, 0]);
sns.violinplot('SEX', 'EDUCATION', data=df[df['default.payment.next.month']==1], ax=axes[2, 1]);
sns.violinplot('EDUCATION', 'MARRIAGE', data=df[df['default.payment.next.month']==0], ax=axes[2, 2]);
sns.violinplot('EDUCATION', 'MARRIAGE', data=df[df['default.payment.next.month']==1], ax=axes[2, 3]);




# In[ ]:




