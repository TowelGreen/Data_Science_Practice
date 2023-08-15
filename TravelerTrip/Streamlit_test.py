import plotly.express as px
import streamlit as st
import pandas as pd


trip_df = pd.read_csv("TravelerTrip.csv")

trip_df = trip_df.dropna()

trip_df['Start date']=pd.to_datetime(trip_df['Start date'])
trip_df['Year'] = trip_df['Start date'].dt.year


year_count=trip_df["Year"].value_counts().reset_index()
year_count=year_count.sort_values(by='Year')

accommodation_count =trip_df["Accommodation type"].value_counts().reset_index()


with st.sidebar:
    theme = st.selectbox("Theme", ["plotly", "ggplot2", "seaborn", "simple_white", "none"])

fig = px.line(year_count, x = 'Year' , y='count', title='Travel based on year',template=theme)
fig2 =px.bar(accommodation_count, x= 'Accommodation type',y='count', title='Accommodation ',template=theme)
fig3 = px.pie(trip_df, names='Transportation type', title='Transportation type',template=theme)

fig.update_layout(
   xaxis = dict(
      tickmode = 'linear',
      tick0 = 1,
      dtick = 0
   )
)

st.write("TravelTrip DashBoard")

#layout



col1 = st.columns(1)
container1 = st.container()



with container1:
        st.plotly_chart(fig, use_container_width=True)

col2, col3 = st.columns(2)
container2 = st.container()

with container2:
    
    with col2:
        st.plotly_chart(fig2, use_container_width=True)

    with col3:
        st.plotly_chart(fig3, use_container_width=True)
  



  

