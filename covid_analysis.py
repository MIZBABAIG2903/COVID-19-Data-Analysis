import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("covid_global_2020-2021.csv")

# Clean data
df = df.dropna(subset=['Recovered', 'Deaths', 'Confirmed'])
df['Recovery_Rate'] = df['Recovered'] / df['Confirmed'] * 100

# Calculate pre/post vaccine recovery rates
pre_vaccine = df[df['Date'] < '2021-01-01']
post_vaccine = df[df['Date'] >= '2021-01-01']

recovery_boost = (post_vaccine['Recovery_Rate'].mean() - 
                  pre_vaccine['Recovery_Rate'].mean()) / pre_vaccine['Recovery_Rate'].mean() * 100

print(f"Recovery accelerated by {recovery_boost:.0f}% post-vaccine")

# Create visualization
fig = px.line(df, x='Date', y='Recovery_Rate', 
              title='Global COVID-19 Recovery Rate Trend')
fig.write_html('recovery_trend.html')
