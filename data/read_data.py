#hint - use those lines of code to read the csv files into a dataframe

df_cov = pd.read_csv("data/covid_de.csv", parse_dates=["date"])
df_vac = pd.read_csv("data/covid_de_vaccines.csv")
df_demo = pd.read_csv("data/demographics_de.csv")