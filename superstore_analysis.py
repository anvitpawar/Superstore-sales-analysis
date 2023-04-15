from datetime import timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

          
data = pd.read_csv("superstore_data.csv")
#print(data.head)

#data.info()

#Here, I changed the column's type "object" to datetime by using "datetime" module in pandas.
data['Order Date'] = pd.to_datetime(data['Order Date'],dayfirst=True)
data['Ship Date'] = pd.to_datetime(data['Ship Date'],dayfirst=True)

# Here I want to choose two columns from dataframe so I have to use two bracket.
print(data[['Order Date', 'Ship Date']].describe().T)

data_daily_sales = data.groupby('Order Date').agg({'Sales':"sum"}).reset_index()
#I grouped  my dataset by "Order Date" and I want that according to "Sales" sum.
#data_daily_sales 
data.groupby(['Order Date', 'Ship Mode']).agg({'Sales':'sum'})
#I just want to see the "Ship Mode" and "Order Date" together.

#fig = px.line(data_daily_sales, x='Order Date', y='Sales', title='Daily Sales')
#fig.show()
data['Sales']=data['Sales'].astype(int)
data_daily_sale = data[data['Sales'] <= 100]
sns.lineplot(x='Order Date', y='Sales',data=data_daily_sale).set(title="Daily Sales")
plt.xticks(rotation=45)
plt.show()
#Generally, using line graph is more logical for daily information.
# I can say that seasonality(christmas- black friday extc) is not included in this data as it is a store that are selling office supplies.

