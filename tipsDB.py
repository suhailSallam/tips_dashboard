## Importing Libraries
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

## loading data
df = pd.read_csv('tips.csv')

st.set_page_config(page_title='Tips Dashboard',page_icon=None,
                   layout='wide',initial_sidebar_state='auto', menu_items=None)
## Sidebar
st.sidebar.header('Tips Dashboard')
st.sidebar.image('tips.jpg')
st.sidebar.write('This Dashboard is for total pills and their tips')
st.sidebar.write('')
st.sidebar.write('Filter your Data')
options_A = st.sidebar.selectbox('Select Base Categorical Option',['sex','smoker','day','time'], key = 'A')
options_B = st.sidebar.selectbox('Select Sub Categorical Option',[None,'sex','smoker','day','time'], key = 'B')
options_C = st.sidebar.selectbox('Select Numerical Option',['total_bill','tip','price_per_person'], key = 'C')
row_filter = st.sidebar.selectbox('Select row    filter',['sex','smoker','day','time'])
col_filter = st.sidebar.selectbox('Select column filter',['sex','smoker','day','time'])

st.sidebar.write('')
st.sidebar.markdown('Made with :heart: by: [Suhail Sallam](https://www.youtube.com/@suhailsallam)')

## body
# row a
a1, a2, a3, a4 = st.columns(4)
a1.metric('Max. Total Bill',df['total_bill'].max())
a2.metric('Max. Tip',df['tip'].max())
a3.metric('Min. Total Bill',df['total_bill'].min())
a4.metric('Min. Tip',df['tip'].min())

# row b
st.subheader('Total Bills VS tips')
fig = px.scatter(data_frame = df,
                 x='total_bill',
                 y='tip',
                 color = options_A,
                 size = options_C,
                 facet_col = col_filter,
                 facet_row = row_filter)
st.plotly_chart(fig,use_container_width=True)

#row c
c1, c2, c3 = st.columns((4,3,3))
with c1:
    st.write('Categorical Vs Numerical')
    fig = px.bar(data_frame=df,
                 x=options_A,
                 y=options_C,
                 color=options_B )
    st.plotly_chart(fig,use_container_width=True)
    
    
with c2:
    st.write('Categorical Vs Numerical')
    fig = px.pie(data_frame=df,
                 names=options_A,
                 values=options_C,
                 color=options_B )
    st.plotly_chart(fig,use_container_width=True)
with c3:
    st.write('Categorical Vs Numerical')
    fig = px.pie(data_frame=df,
                 names=options_A,
                 values=options_C,
                 color=options_B,
                 hole=0.4)
    st.plotly_chart(fig,use_container_width=True)

