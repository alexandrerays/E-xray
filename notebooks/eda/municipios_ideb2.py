#!/usr/bin/env python
# coding: utf-8

# Esse notebook faz a junção de cada dataset de município com a coluna do `ideb` do dataset do ideb. O objetivo dessa junção é analisar como as variáveis de municípios impactam no ideb, que é a nossa variável resposta. 

# # Bibliotecas

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats


# In[2]:


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


# # Carrega Datasets

# In[3]:


df_municipios_2015 = pd.read_csv('../../data/bcggammachallenge/municipios/municipios20150101.csv')
df_municipios_2016 = pd.read_csv('../../data/bcggammachallenge/municipios/municipios20160101.csv')
df_municipios_2017 = pd.read_csv('../../data/bcggammachallenge/municipios/municipios20170101.csv')


# In[4]:


df = pd.concat([df_municipios_2015, df_municipios_2016, df_municipios_2017])


# In[5]:


df_municipios_2017.shape


# In[6]:


df.head()


# In[7]:


df_ideb_ini = pd.read_csv('../../data/bcggammachallenge/ideb/ideb_municipios_anosiniciais2005_2017.csv',sep = ',',encoding='latin-1')
df_ideb_fin = pd.read_csv('../../data/bcggammachallenge/ideb/ideb_municipios_anosfinais2005_2017.csv',sep = ',',encoding='latin-1')


# In[8]:


df_ideb_ini.shape


# In[9]:


df_ideb_ini.columns


# In[10]:


df_ideb_fin.columns


# In[11]:


df_ideb_ini[['Cod_Municipio_Completo', 'Ideb2017']].head()


# In[12]:


df_ideb_ini = df_ideb_ini.rename(columns={'Cod_Municipio_Completo': 'cod_municipio'})
df_ideb_fin = df_ideb_fin.rename(columns={'Cod_Municipio_Completo': 'cod_municipio'})

df_ideb_ini_2015 = df_ideb_ini.copy()
df_ideb_ini_2017 = df_ideb_ini.copy()

df_ideb_fin_2015 = df_ideb_fin.copy()
df_ideb_fin_2017 = df_ideb_fin.copy()


# In[13]:


df_ideb_ini_2015 = df_ideb_ini_2015[['cod_municipio', 'Ideb2015']]
df_ideb_ini_2017 = df_ideb_ini_2017[['cod_municipio', 'Ideb2017']]

df_ideb_fin_2015 = df_ideb_fin_2015[['cod_municipio', 'Ideb2015']]
df_ideb_fin_2017 = df_ideb_fin_2017[['cod_municipio', 'Ideb2017']]


# In[14]:


df_ideb_ini_2015.head()


# In[15]:


df_ideb_ini_2017.head()


# In[16]:


df_ideb_fin_2015.head()


# In[17]:


df_ideb_fin_2017.head()


# In[18]:


df_ideb_ini_2015['cod_municipio'] = df_ideb_ini_2015.cod_municipio.astype(float)
df_ideb_ini_2017['cod_municipio'] = df_ideb_ini_2017.cod_municipio.astype(float)

df_ideb_fin_2015['cod_municipio'] = df_ideb_fin_2015.cod_municipio.astype(float)
df_ideb_fin_2017['cod_municipio'] = df_ideb_fin_2017.cod_municipio.astype(float)


# In[19]:


df_result_ini_2015 = pd.merge(df_municipios_2015, df_ideb_ini_2015, how='inner', on='cod_municipio')
df_result_ini_2017 = pd.merge(df_municipios_2017, df_ideb_ini_2017, how='inner', on='cod_municipio')

df_result_fin_2015 = pd.merge(df_municipios_2015, df_ideb_fin_2015, how='inner', on='cod_municipio')
df_result_fin_2017 = pd.merge(df_municipios_2017, df_ideb_fin_2017, how='inner', on='cod_municipio')


# In[20]:


df_result_ini_2015 = df_result_ini_2015.rename(columns={'Ideb2015': 'ideb'})
df_result_ini_2017 = df_result_ini_2017.rename(columns={'Ideb2017': 'ideb'})

df_result_fin_2015 = df_result_fin_2015.rename(columns={'Ideb2015': 'ideb'})
df_result_fin_2017 = df_result_fin_2017.rename(columns={'Ideb2017': 'ideb'})


# In[21]:


df_result_ini_2015.sort_values(by=['ideb'], ascending=False).head(8)


# In[22]:


df_result_ini_2017.sort_values(by=['ideb'], ascending=False).head(8)


# In[23]:


df_result_fin_2015.sort_values(by=['ideb'], ascending=False).head(8)


# In[24]:


df_result_fin_2017.sort_values(by=['ideb'], ascending=False).head(8)


# ## Limpeza do Ideb

# In[25]:


df_result_ini_2015.drop(df_result_ini_2015[df_result_ini_2015.ideb == '-'].index, inplace=True)
df_result_ini_2017.drop(df_result_ini_2017[df_result_ini_2017.ideb == '-'].index, inplace=True)
df_result_fin_2015.drop(df_result_fin_2015[df_result_fin_2015.ideb == '-'].index, inplace=True)
df_result_fin_2017.drop(df_result_fin_2017[df_result_fin_2017.ideb == '-'].index, inplace=True)


# In[26]:


df_result_ini_2015['ideb'] = pd.to_numeric(df_result_ini_2015['ideb'])
df_result_ini_2017['ideb'] = pd.to_numeric(df_result_ini_2017['ideb'])

df_result_fin_2015['ideb'] = pd.to_numeric(df_result_fin_2015['ideb'])
df_result_fin_2017['ideb'] = pd.to_numeric(df_result_fin_2017['ideb'])


# In[27]:


print(df_result_ini_2015.shape)
print(df_result_fin_2015.shape)
print(df_result_ini_2017.shape)
print(df_result_fin_2017.shape)


# # Correlação linear entre todas as variáveis numéricas com o Ideb

# In[28]:


def calculate_pearson(df):
    correlations = {}
    numerical_features = df.select_dtypes(exclude = ["object"]).columns
    numerical_features = numerical_features.drop("cod_municipio")
    for i in numerical_features:
        corr = stats.pearsonr(df[i], df['ideb'])[0]
        correlations[i] = corr
    df_corr = pd.DataFrame(list(correlations.items()), columns=['feature', 'correlation_with_ideb'])        
    df_corr = df_corr.dropna()
    
    return df_corr


# In[29]:


df_corr_ini_2015 = calculate_pearson(df_result_ini_2015)
df_corr_ini_2017 = calculate_pearson(df_result_ini_2017)

df_corr_fin_2015 = calculate_pearson(df_result_fin_2015)
df_corr_fin_2017 = calculate_pearson(df_result_fin_2017)


# In[30]:


df_corr_ini_2015.sort_values(by=['correlation_with_ideb'], ascending=False)


# In[31]:


df_corr_ini_2017.sort_values(by=['correlation_with_ideb'], ascending=False)


# In[32]:


df_corr_fin_2015.sort_values(by=['correlation_with_ideb'], ascending=False)


# In[33]:


df_corr_fin_2017.sort_values(by=['correlation_with_ideb'], ascending=False)


# ## Separa anos iniciais de anos finais

# In[34]:


df_result_ini_2015.filter(like='medio').columns


# In[35]:


df_result_ini_2015 = df_result_ini_2015.drop(df_result_ini_2015.filter(like='medio').columns, axis=1)
df_result_ini_2017 = df_result_ini_2017.drop(df_result_ini_2017.filter(like='medio').columns, axis=1)


# In[36]:


df_result_fin_2015.filter(like='fund').columns


# In[37]:


df_result_fin_2015 = df_result_fin_2015.drop(df_result_fin_2015.filter(like='fund').columns, axis=1)
df_result_fin_2017 = df_result_fin_2017.drop(df_result_fin_2017.filter(like='fund').columns, axis=1)

df_result_fin_2015 = df_result_fin_2015.drop(['num_estudantes_ensino_infantil'], axis=1)
df_result_fin_2017 = df_result_fin_2017.drop(['num_estudantes_ensino_infantil'], axis=1)


# In[38]:


print(df_result_ini_2015.shape)
print(df_result_ini_2017.shape)
print(df_result_fin_2015.shape)
print(df_result_fin_2017.shape)


# ## Salvar

# In[39]:


df_result_ini_2015.to_csv('../../data/bases_ale/ideb_municipios_2015_ai.csv')
df_result_ini_2017.to_csv('../../data/bases_ale/ideb_municipios_2017_ai.csv')
df_result_fin_2015.to_csv('../../data/bases_ale/ideb_municipios_2015_af.csv')
df_result_fin_2017.to_csv('../../data/bases_ale/ideb_municipios_2017_af.csv')

