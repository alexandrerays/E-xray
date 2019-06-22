#!/usr/bin/env python
# coding: utf-8

# # BCG Gamma Challenge

# # Libraries

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats


# In[2]:


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


# # Dataset

# In[3]:


df_municipios_2015 = pd.read_csv('bcggammachallenge/municipios/municipios20150101.csv')


# In[4]:


df_municipios_2016 = pd.read_csv('bcggammachallenge/municipios/municipios20160101.csv')


# In[5]:


df_municipios_2017 = pd.read_csv('bcggammachallenge/municipios/municipios20170101.csv')


# In[6]:


df_municipios_2015.shape


# In[7]:


df_municipios_2016.shape


# In[8]:


df_municipios_2017.shape


# In[9]:


df = pd.concat([df_municipios_2015, df_municipios_2016, df_municipios_2017])


# In[10]:


df.shape


# In[11]:


df.head(5)


# In[12]:


df_ideb_ini = pd.read_csv('bcggammachallenge/ideb/ideb_municipios_anosiniciais2005_2017.csv',sep = ',',encoding='latin-1')


# In[13]:


df_ideb_ini.columns


# In[14]:


df_ideb_ini[['Cod_Municipio_Completo', 'Ideb2017']].head()


# In[15]:


df_ideb_ini = df_ideb_ini.rename(columns={'Cod_Municipio_Completo': 'cod_municipio'})


# In[16]:


df_ideb_ini_2015 = df_ideb_ini.copy()


# In[17]:


df_ideb_ini = df_ideb_ini[['cod_municipio', 'Ideb2017']]


# In[18]:


df_ideb_ini_2015 = df_ideb_ini_2015[['cod_municipio', 'Ideb2015']]


# In[19]:


df_ideb_ini.head()


# In[20]:


df_ideb_ini_2015.head()


# In[21]:


df_ideb_ini['cod_municipio'] = df_ideb_ini.cod_municipio.astype(float)
df_ideb_ini_2015['cod_municipio'] = df_ideb_ini_2015.cod_municipio.astype(float)


# In[22]:


df_result_2017 = pd.merge(df_municipios_2017, df_ideb_ini, how='inner', on='cod_municipio')
df_result_2015 = pd.merge(df_municipios_2015, df_ideb_ini_2015, how='inner', on='cod_municipio')


# In[23]:


df_result_2017.head()


# In[ ]:





# In[24]:


df_result_2015 = df_result_2015.rename(columns={'Ideb2015': 'ideb'})
df_result_2017 = df_result_2017.rename(columns={'Ideb2017': 'ideb'})


# In[25]:


df_result_2015.shape


# In[26]:


df_result_2017.shape


# In[27]:


df_result_2015.head()


# In[28]:


df_result_2017.head()


# In[30]:


df = pd.concat([df_result_2015, df_result_2017])


# In[31]:


df.shape


# In[56]:


df['ano_censo'].head()


# In[80]:


df['ideb'].head()


# In[97]:


df['ideb'] = df.ideb.apply(lambda x: x.replace('-',''))


# In[98]:


df['ideb'] = df['ideb'].replace('', 0)


# In[84]:


df_ideb[df_ideb['Ideb2017'] != '-']['Ideb2017'].order


# In[ ]:


df_ideb[df_ideb['Ideb2017'] != '-']['Ideb2017'].min()


# In[ ]:


df_ideb.sort_values(by=['Ideb2017'], ascending=False).head(10)


# In[ ]:




