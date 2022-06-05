#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import streamlit as st


# In[3]:



if st.checkbox('Show dataframe'):
    st.write(df)


# In[6]:


# options = st.multiselect(
#  'Which Employee Are You Looking For?', df['Employee'].unique())
# st.write('You selected:', options)


# In[8]:


df = pd.read_csv("progress_report.csv")
Employees = st.multiselect('Show Player for clubs?', df['Employee'].unique())
# nationalities = st.multiselect('Show Player from Nationalities?', df['Nationality'].unique())
# Filter dataframe
new_df = df[(df['Employee'].isin(Employees))]
# write dataframe to screen
st.write(new_df)


# In[ ]:




