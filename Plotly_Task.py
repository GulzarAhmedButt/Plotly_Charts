#!/usr/bin/env python
# coding: utf-8

# In[125]:


import pandas as pd
import numpy as np
import seaborn as sns
import datetime as dt
import plotly.graph_objects as go
import plotly.express as px
import chart_studio.tools as tls
import plotly.io as pio
import chart_studio
import chart_studio.plotly as py


# In[96]:


from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot


# In[97]:


import cufflinks as cf
init_notebook_mode(connected=True)
get_ipython().run_line_magic('matplotlib', 'inline')


# In[98]:


time_data = pd.read_csv('time data.csv')
call_data = pd.read_csv('call_log_export.csv')


# In[99]:


calender_data = pd.read_csv('calendar data.csv')


# In[100]:


calender_data['Days in Week'] = calender_data['Days in Week'].astype('category')


# In[101]:


dicti = {'Day':calender_data['Days in Week'],'Time':time_data['Hour'],'call_id':call_data['call_id']}


# In[102]:


dataset = pd.DataFrame(data=dicti)
dataset


# In[103]:


dataset_new = dataset.drop(dataset.index[1440:])


# In[104]:


dataset_new['Time']=dataset_new['Time'].astype(int)


# In[105]:


data = dataset_new.sort_values('Time',ascending=True)
data


# In[106]:


final_data = data[(data['Time']>6) & (data['Time']<19)]
final_data


# In[107]:


final_data.dtypes


# In[108]:


fig1 = go.Figure(data=[go.Scatter(
    x=final_data['Time'],
    y=final_data['Day'],
    mode='markers',
    marker=dict(
        size=final_data['call_id'],
        sizemode='area',
        sizeref= 4.*max(final_data['call_id'])/(25.**2),
        sizemin=4)
)])

fig1.update_xaxes(title_text='Time (7AM to 6PM)')
fig1.update_yaxes(title_text='Day')


fig1.show()


# In[109]:


dataset_2 = pd.read_csv('call_log_export.csv')


# In[110]:


dataset_2_v2 = dataset_2[dataset_2['Start_Time'].notnull()]


# In[111]:


dicti_call_v2 = {'call':dataset_2_v2['call_id'],'Time':time_data['Hour']}


# In[112]:


Data_final_v2 = pd.DataFrame(data=dicti_call_v2)


# In[113]:


second_data_v2 = Data_final_v2[Data_final_v2['Time'].notnull()]
second_data_v2


# In[114]:


second_data_v2.groupby('Time')


# In[115]:


second_data_v3 = second_data_v2.groupby('Time')


# In[116]:


second_data_v4 = second_data_v3.sum()
second_data_v3.dtypes


# In[117]:


second_data_v4.reset_index(inplace=True)


# In[118]:


second_data_v5 = second_data_v4[(second_data_v4['Time']>6)&(second_data_v4['Time']<19)]


# In[119]:


fig = go.Figure(data=go.Scatter(x=second_data_v5['Time'],
                                y=second_data_v5['call'],
                                mode='lines+markers',
                                marker_symbol='circle',
                                marker=dict(size=10),
                                line=dict(dash='dash')))


fig.update_xaxes(title_text='Time (7AM to 6PM)')
fig.update_yaxes(title_text='# Of Calls')

fig.show()


# In[120]:


pio.write_html(fig1, file='chart1.html', auto_open=True)
pio.write_html(fig, file='chart2.html', auto_open=True)


# In[124]:


username='tintlbiz123'
api_key='WpuYXQcsgnTqPVsNB4GN'
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)


# In[126]:


py.plot(fig1, filename = 'chart1_bubble', auto_open=True)
py.plot(fig, filename = 'chart2_line', auto_open=True)


# In[128]:


tls.get_embed('https://plot.ly/~tintlbiz123/8/#/') 


# In[129]:


tls.get_embed('https://plot.ly/~tintlbiz123/10/#/') 


# In[ ]:




