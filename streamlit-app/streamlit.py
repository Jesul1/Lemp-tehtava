import streamlit as st
import pandas as pd
import plotly.express as px


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

if __name__ == "__main__":
    main()