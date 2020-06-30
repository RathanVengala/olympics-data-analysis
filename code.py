# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
# Data Loading 

data.head(10)
# Summer or Winter

data['Better_Event']=np.where(data['Total_Summer']>=data['Total_Winter'],'Summer','Winter')


data['Better_Event'][77]='both'
better_event=data['Better_Event'].value_counts().idxmax()

# Top 10

top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

top_countries.drop(top_countries.tail(1).index,inplace=True)


def top_ten(top_countries,col):
    top=top_countries.nlargest(10,col)
    country_list=top['Country_Name']
    return country_list
top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')
common=list(set(top_10).intersection(set(top_10_summer),set(top_10_winter)))

# Plotting top 10
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]

fig,(ax_1,ax_2,ax_3)=plt.subplots(1,3, figsize=(30,10))
summer_df.plot(x='Country_Name', y= 'Total_Summer',kind='bar',ax=ax_1)
ax_1.set_title('Summer Medal Count')

winter_df.plot(x='Country_Name',y='Total_Winter',kind='bar',ax=ax_2)
ax_2.set_title('Winter Medal Count')

top_df.plot(x='Country_Name',y='Total_Medals',kind='bar',ax=ax_3)
ax_3.set_title('Total Medal Count')
# Top Performing Countries
summer_df["Golden_Ratio"]=(summer_df['Gold_Summer']/summer_df['Total_Summer'])
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold=summer_df['Country_Name'][summer_df['Golden_Ratio'].idxmax()]
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold=winter_df['Country_Name'][winter_df['Golden_Ratio'].idxmax()]
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold=top_df['Country_Name'][top_df['Golden_Ratio'].idxmax()]
data_1=pd.DataFrame(data.drop(data.tail(1).index))
data_1['Total_Points']=data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']
most_points=data_1['Total_Points'].max()
best_country=data_1['Country_Name'][data_1['Total_Points'].idxmax()]

# Plotting the best


best=data[data['Country_Name']==best_country]

best=best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot(kind='bar',stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)




