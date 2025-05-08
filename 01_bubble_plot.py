import plotly.express as px
# Load the data set
df = px.read_csv('C:\Users\ABHISHEK\Desktop\Tools & Methods of Data Analysis\population_current.csv')

fig = px.scatter(df.query("year==2023"), x="gdpPercap", y="lifeExp",
	         size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)
fig.show()
