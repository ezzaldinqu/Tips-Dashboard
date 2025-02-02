from os import write

import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go



# Load Data
df_tips = pd.read_csv('tips.csv')

st.set_page_config(page_title='Tips Dashboard',layout='wide',initial_sidebar_state='auto')
# Title
st.sidebar.header('Tips Dashboard')

# Side Bar
st.sidebar.image('tips.jpeg')
st.sidebar.write('This Dashboard is using Tips dataset from seaborn for educational purposes.')
st.sidebar.write('')
st.sidebar.write('Filter your data')
category_filter = st.sidebar.selectbox('Categorical',[None,'sex','smoker','day','time'])
numerical_filter = st.sidebar.selectbox('Numerical Filter',[None,'total_bill','tip'])
column_filter = st.sidebar.selectbox('Column Filter',[None,'smoker'])
row_filter = st.sidebar.selectbox('Row Filter',[None,'sex'])

st.sidebar.markdown('Made with Love :heart_eyes: by [Ezzeddin Qubaitari](https://business-intelligence.online/)')

# Body
# Define columns
# row A
a1,a2,a3,a4 = st.columns(4)
a1.metric('Max. Total Bill',df_tips['total_bill'].max())
a2.metric('Max. Tip',df_tips['tip'].max())
a3.metric('Min. Total Bill',df_tips['total_bill'].min())
a4.metric('Min. Tip',df_tips['tip'].min())

#Row B
st.subheader('Total Bills vs. Tips')
fig = px.scatter(data_frame=df_tips,
                 x='total_bill',
                 y='tip',
                 color=category_filter,
                 size=numerical_filter,
                 facet_col=column_filter,
                 facet_row=row_filter)
st.plotly_chart(fig,use_container_width=True)

# Row C Add Table
# Create the table
fig2 = go.Figure(data=[go.Table(
    header=dict(values=list(df_tips.columns), fill_color='lightgray', align='left'),
    cells=dict(values=[df_tips[col] for col in df_tips.columns], align='left')
)])
st.plotly_chart(fig2,use_container_width=True)

# Row C
# (4,3,3) to specify the first column 40% , second 30% the third 30%
c1,c2,c3 = st.columns((4,3,3))

with c1:
    st.text('Sex vs. Total Bills')
    fig = px.bar(data_frame=df_tips,x='sex',y='total_bill',color=category_filter)
    st.plotly_chart(fig,use_container_width=True)
with c2:
    st.text('Smoker/Non-Smoker vs. Tips')
    fig = px.pie(data_frame=df_tips,names='smoker',values='tip',color=category_filter)
    st.plotly_chart(fig,use_container_width=True)
with c3:
    st.text('Days vs. Tips')
    fig = px.pie(data_frame=df_tips, names='day', values='tip', color=category_filter,hole=0.4)
    st.plotly_chart(fig, use_container_width=True)
