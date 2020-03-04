# documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html
df_year = df_rural.columns.drop(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code']).tolist()
df_id = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code']
df_rural = pd.melt(df_rural, id_vars=df_id, value_vars=df_year,
        var_name='Year', value_name='Rural Value')

df_electricity = pd.melt(df_electricity, id_vars=df_id, value_vars=df_year,
        var_name='Year', value_name='Electricity Value')
