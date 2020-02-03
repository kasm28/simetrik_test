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
base = pd.read_fwf('prueba_txt.txt', header=None)


# In[3]:


base.head()


# In[4]:


#eliminamos la columna sin valores
base = base.drop(2, axis=1)
base.dtypes


# In[5]:


#insertamos la columna de consecutivo
base.insert(4, 'Consecutivo', range(1, 1 + len(base)))
base.head()


# In[6]:


#insertamos la columna con la fecha requerida
base['Fecha']= pd.to_datetime("'06-07-2019'", dayfirst=True)
base.head()


# In[7]:


#cambiamos los nombres de las columnas 
base.columns = ['Marca', 'Tipo', 'Ubicacion', 'Placa', 'Consecutivo', 'Fecha']
base.head()


# In[8]:


base.dtypes


# In[9]:


#una vez realizados los cambios a la base de datos la exportamos a .csv
base.to_csv('2do_punto_prueba.csv', index=False, header=True, encoding="utf-8")

