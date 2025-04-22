import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv(r"C:\Users\ABHISHEK\Desktop\Tools_Methods_Data_Analysis\annual_deforestation.csv")

# Filter for year 2015 and drop rows without ISO codes
df_1990 = df[(df["Year"] == 1990) & (df["Code"].notna()) & (df["Code"]!='OWID_WRL')]

# Create choropleth map
fig = px.choropleth(
    df_1990,
    locations="Code",  # ISO Alpha-3 codes
    color="Deforestation",
    hover_name="Entity",
    color_continuous_scale="Reds",
    range_color= [0, 1000000],
    projection="natural earth",
    title="Annual Deforestation by Country (1990)",
    labels={'Deforestation': 'Hectares'}
)

df_2015 = df[(df["Year"] == 2015) & (df["Code"].notna())]

# Create choropleth map
fig_2 = px.choropleth(
    df_2015,
    locations="Code",  # ISO Alpha-3 codes
    color="Deforestation",
    hover_name="Entity",
    color_continuous_scale="Reds",
    range_color= [0, 1000000],
    projection="natural earth",
    title="Annual Deforestation by Country (2015)",
    labels={'Deforestation': 'Hectares'}
)

fig.update_layout(geo=dict(showframe=False, showcoastlines=True))
fig.show()

fig_2.update_layout(geo=dict(showframe=False, showcoastlines=True))
fig_2.show()

df_1990
