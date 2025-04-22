import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv(r"C:\Users\ABHISHEK\Desktop\Tools_Methods_Data_Analysis\annual_deforestation.csv")  # Make sure the file is in your working directory

# Filter the data for 1990–2015 and drop rows with missing ISO codes
df_range = df[(df["Year"] >= 1990) & (df["Year"] <= 2015) & (df["Code"].notna())]

# Create animated choropleth map
fig = px.choropleth(
    df_range,
    locations="Code",
    color="Deforestation",
    hover_name="Entity",
    color_continuous_scale="Reds",
    range_color= [0, 1000000],
    animation_frame="Year",
    projection="natural earth",
    title="🌍 Annual Deforestation by Country (1990–2015)",
    labels={'Deforestation': 'Hectares'}
)

fig.layout.updatemenus[0].buttons[0].args[1]['frame'] = {'duration': 1000, 'redraw': True}
fig.layout.updatemenus[0].buttons[0].args[1]['transition'] = {'duration': 500}

fig.update_layout(geo=dict(showframe=False, showcoastlines=True))
fig.show()
