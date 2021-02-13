#This is the code-only version of the Jupyter notebook. Please see the Jupyter notebook (flight_data_analysis.ipynb) for comments, explanations, and acknowledgments.

import pandas as pd
df = pd.read_csv("../flights.csv")
print(df.head(10))
print(df.tail(10))
print(df.shape) 
print(df.size) 
print(df.info())
airlines_array = df['AIRLINE'].unique()
for airline in airlines_array:
    print(airline)
airline_arrival_delay_data = {}
for airline in airlines_array:
    airline_dict = {}
    mean_arrival_delay = df[(df.AIRLINE==airline) & (df.ARRIVAL_DELAY > 0)].ARRIVAL_DELAY.mean()
    proportion_delayed = df[(df.AIRLINE==airline) & (df.ARRIVAL_DELAY > 0)].AIRLINE.count()/df[(df.AIRLINE==airline)].AIRLINE.count()
    delay_expected_value = mean_arrival_delay*proportion_delayed
    print("Average arrival delay (among delays greater than 0) for" , airline, mean_arrival_delay)
    airline_dict ['mean_arrival_delay'] = mean_arrival_delay 
    airline_dict ['proportion_delayed'] = proportion_delayed
    airline_dict ['delay_expected_value'] = delay_expected_value
    airline_arrival_delay_data[airline] = airline_dict
print(airline_arrival_delay_data) 
df_airline_delay_data = pd.DataFrame.from_dict(airline_arrival_delay_data).transpose()
df_airline_delay_data.rename_axis("airline",inplace=True)
print(df_airline_delay_data)
df_airline_delay_data.sort_values('delay_expected_value',ascending=False,inplace=True)
print(df_airline_delay_data)
df_airline_delay_data.to_csv('airline_delay_data.csv')
simpler_delay_comparison = {}
for airline in airlines_array:
    mean_arrival_delay = df[(df.AIRLINE==airline)].ARRIVAL_DELAY.mean()
    simpler_delay_comparison[airline]=mean_arrival_delay
print(simpler_delay_comparison)
simpler_delay_table = pd.DataFrame.from_dict(simpler_delay_comparison,orient='index',columns=['mean_arrival_delay'])
simpler_delay_table.sort_values('mean_arrival_delay',ascending=False,inplace=True)
df_airline_delay_data.rename_axis("airline",inplace=True)
print(simpler_delay_table)