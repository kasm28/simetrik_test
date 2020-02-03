#!/usr/bin/env python
# coding: utf-8

# ### 1. Data Preparation

# In[1]:


# importing modules
import pandas as pd
import numpy as np
import locale
from datetime import datetime as dt
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#Displaying all dataframe columns
pd.set_option('display.max_columns', None)


# In[2]:


#Loading datasets
datos = pd.read_excel('consumo_prueba_2019.xls', skiprows=7, header=None)


# In[3]:


datos.head(20)


# In[4]:


datos.columns = datos.iloc[1]
datos = datos.drop(datos.index[[1, 8, 14]])


# In[5]:


datos = datos.dropna(axis=1, how='all')
datos = datos.dropna(axis=0, thresh=10)
datos.head(20)


# In[6]:


datos = datos.dropna(axis=1, how='all')
datos['Cliente'] = "COLS" 
datos.head(20)


# In[7]:


datos['Estacion'] = "00 SOL"
datos.loc[(datos.index[4:7], 'Estacion')] = "01 AIRES"
datos.loc[(datos.index[7:13], 'Estacion')] = "02 URT"


# In[8]:


datos.head(30)


# In[9]:


locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
#debemos convertir la fecha a datetime
datos['Fecha'] = pd.to_datetime(datos['Fecha'], format='%d%b%Y:%H:%M:%S')
datos.head(30)


# In[10]:


#una vez realizados los cambios a la base de datos la exportamos a .csv
datos.to_csv('3er_punto_prueba.csv', index=False, header=True, encoding="utf-8")

