# https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html
df_projects['countryname'].str.split(';', expand=True).iloc[:, 0]
