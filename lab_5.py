import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt



data = pd.read_csv("https://github.com/hwahoh/CSE5544-lab-final/blob/438797bb4119358b632991281763ec24273a9b45/qs-world-university-rankings-2017-to-2022-V2.csv?raw=true")


dv1 = data.drop(columns=['link','logo'])
dv1['score'] = dv1['score'].apply(pd.to_numeric, errors='coerce')
#dv1['year'] = dv1['year'].apply(pd.to_numeric, errors='coerce', downcast='integer')
regions = dv1['region'].drop_duplicates()
region_choice = st.selectbox('Select your universities:', regions)
countries = dv1['country'].loc[dv1['region'] == region_choice].drop_duplicates()
country_choice = st.selectbox('', countries)

dv1 = dv1[dv1['country'] == country_choice]
chart1 = alt.Chart(dv1).mark_line().encode(
    x='year:N',
    y='score',
    color='university',
    tooltip= ['year', 'university', 'score','student_faculty_ratio', 'type', 'research_output']
)

st.altair_chart(chart1, use_container_width=True)
