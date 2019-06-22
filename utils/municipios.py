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


df_municipios_2015 = pd.read_csv('../bcggammachallenge/municipios/municipios20150101.csv')


# In[4]:


df_municipios_2016 = pd.read_csv('../bcggammachallenge/municipios/municipios20160101.csv')


# In[5]:


df_municipios_2017 = pd.read_csv('../bcggammachallenge/municipios/municipios20170101.csv')


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


df.head(10)


# In[12]:


df['regiao'].value_counts()


# In[13]:


df['ano_censo'].value_counts()


# In[14]:


df[df['municipio'] == 'Jussara']


# In[15]:


columns = [
    'ano_censo',
    'regiao',
    'unidade_federativa',
    'municipio',
    'num_escolas',
    'num_escolas_em_atividade',
    'num_professores',
    'num_estudantes',
    'num_funcionarios'    
]

df[columns].head()


# In[16]:


df[columns].describe()


# In[17]:


df.columns


# In[18]:


df['cod_municipio'].dtypes


# In[19]:


df.head()


# In[ ]:




