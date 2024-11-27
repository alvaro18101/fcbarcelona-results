import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import stats

df = pd.read_csv('processed_matches.csv')
df_stats = pd.read_csv('data.csv')

st.title('FC Barcelona')

st.header('Tabulated Results')
st.write('Data extracted from https://www.365scores.com/es/football/team/fc-barcelona-132 and processed with Pandas')
st.write(df)

st.header('Stats')
st.subheader('Tabulated Stats')
st.write(df_stats)

st.subheader('Bar Chart')
st.pyplot(stats.fig1)
st.pyplot(stats.fig2)
numero = stats.counts[0]/sum(stats.counts)

st.write(f'Victories: {"%.2f" % float(100*stats.counts[0]/sum(stats.counts))}%')
st.write(f'Defeats: {"%.2f" % float(100*stats.counts[1]/sum(stats.counts))}%')
st.write(f'Tiers: {"%.2f" % float(100*stats.counts[2]/sum(stats.counts))}%')

st.subheader('Cumulative Goals Difference')
st.pyplot(stats.fig3)


st.subheader('Home and away stats')
st.pyplot(stats.fig4)
# st.info('Informations')