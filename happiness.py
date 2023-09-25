import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
URL = "https://raw.githubusercontent.com/aliannan99/aliapp/main/happiness.csv"
file_path = URL
df = pd.read_csv(file_path)
st.title("Happiness, Does it exist and where?")
st.write("Happiness can be found even in the darkest of places, if only one rememebers to turn on the light")
fig = px.scatter_geo(
    df,
    locations="Countries",
    locationmode="country names",
    color="Happiness index, 2022",
    hover_name="Countries",
    hover_data=["Happiness index, 2022"],
    projection="natural earth",
    title="World Happiness Index 2022",
)
fig.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white")
show_high_happiness = st.checkbox("Show Countries with Happiness Index >= 6")
show_medium_happiness = st.checkbox("Show Countries with 3 <= Happiness Index < 6")
show_low_happiness = st.checkbox("Show Countries with Happiness Index < 3")
filtered_df = df  

if show_high_happiness:
    filtered_df = filtered_df[filtered_df["Happiness index, 2022"] >= 6]

if show_medium_happiness:
    filtered_df = filtered_df[(filtered_df["Happiness index, 2022"] >= 3) & (filtered_df["Happiness index, 2022"] < 6)]

if show_low_happiness:
    filtered_df = filtered_df[filtered_df["Happiness index, 2022"] < 3]
st.write("### World Map of Happiness Index")
if not filtered_df.empty:
    filtered_fig = px.scatter_geo(
        filtered_df,
        locations="Countries",
        locationmode="country names",
        color="Happiness index, 2022",
        hover_name="Countries",
        hover_data=["Happiness index, 2022"],
        projection="natural earth",
        title="Filtered World Happiness Index 2022",
    )
    filtered_fig.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white")
    st.plotly_chart(filtered_fig)
else:
    st.write("No countries match the selected criteria.")
if not filtered_df.empty:
    st.write("### Filtered Data")
    st.dataframe(filtered_df)

df = df[::-1]
st.title("Click to see the Top 10 happiest countries")
st.write("hint: You wont find Lebanon due to censored circumstances")

fig_global_rank = px.bar(
    df,
    x="Global rank",
    y="Countries",
    text="Countries",  
    title="Global Ranks of Countries",
)


fig_global_rank.update_xaxes(title="Global Rank")


show_top_10 = st.checkbox("Top 10 Happiest Countries", key="top_10", value=False)


if show_top_10:
    filtered_df = df[df["Global rank"] <= 10]
else:
    filtered_df = df


fig_global_rank.update_traces(x=filtered_df["Global rank"], y=filtered_df["Countries"], text=filtered_df["Countries"])


st.plotly_chart(fig_global_rank)
