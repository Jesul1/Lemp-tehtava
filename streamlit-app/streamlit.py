import os
import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector
import requests

@st.cache_resource
def mySql():
    # Initialize connection.
    conn = st.connection('mysql', type='sql')
    # Perform query.
    df = conn.query('SELECT * from temperature_data LIMIT 100;', ttl=600)
    return df
    # Streamlit

def main():
    st.title("Plot data from MySql")
    st.write("Temperature data from exampledb")
    data = mySql()
    #plot data
    df2 = pd.DataFrame(data, columns=["date","temperature"])
    totalKg = px.line(df2, x="date", y="temperature")
    st.plotly_chart(totalKg, use_container_width=True)

    conn = st.connection('mysql', type='sql')
    df = conn.query(
        "SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 50",
        ttl="0"
    )
    st.title('Säädata Oulusta')
    st.dataframe(df)

    def display_cat():
        url = 'https://cataas.com/cat?json=true'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            image_url = data['url']
            st.image(image_url, caption='Cat Image', use_container_width=True)
            # Process the response data as needed
        else:
            print('Request failed with status code:', response.status_code)

    if st.button("Get cat image"):
        display_cat()

if __name__ == "__main__":
    main()