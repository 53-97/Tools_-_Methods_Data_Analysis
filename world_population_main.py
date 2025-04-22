import pandas as pd

statistic_df = pd.read_csv(r"C:\Users\ABHISHEK\Desktop\Tools_Methods_Data Analysis\countries_population.csv", encoding='latin-1',header=1,usecols=range(1,9))

statistic_df.rename(
    columns = {
        statistic_df.columns[0] : 'Region or Country',
        'Value' : 'Urban percentage'
    },
    inplace=True
)