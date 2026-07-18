import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')

# data cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
# print(df.columns.tolist())
df=df.drop_duplicates()

# numerical data cleaning
df['price'] = df['price'].str.replace(',', '').astype(int)
df['rate_per_sqft'] = df['rate_per_sqft'].str.replace(',', '').astype(float)

# categorical data cleaning
df['status'] = df['status'].str.strip().str.lower()
df['property_type'] = df['property_type'].str.strip().str.lower()
df['builder_name'] = df['builder_name'].str.strip().str.lower()
df['locality'] = df['locality'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().map({'Approved by RERA': True, 'Not approved by RERA': False})
df['socity'] = df['socity'].str.strip().str.lower()
df['company_name'] = df['company_name'].str.strip().str.lower()
df['flat_type'] = df['flat_type'].str.strip().str.lower()

# print(df.head())
# print(df.info())

# df.to_csv('cleaned_dataset.csv', index=False) # saving the cleaned dataset to a new CSV file

# insights

# Question 1: Which is the costliest flat?
costliest_flat = df.loc[df['price'].idxmax()]

print(f"The costliest flat is a {costliest_flat['property_type']} located at {costliest_flat['locality']} in {costliest_flat['socity']} society, priced at {costliest_flat['price']}.")


# Q2 : Which locality has the highest average price?

costliest_locality = df.groupby('locality')['price'].mean().idxmax()
print(f"{costliest_locality} has the highest average price of {df.groupby('locality')['price'].mean().max():.2f}")

# Q3 : Which locality has the highest rate per square foot?
costliest_localitybySqfeet = df.groupby('locality')['rate_per_sqft'].max().idxmax()
print(f"{costliest_localitybySqfeet} has the highest rate per sqft of {df.groupby('locality')['rate_per_sqft'].max().max()}")

# Q4 : Are ready to move flats more expensive than under construction flats on average?
rtm_avg_price = df[df['status'] == 'ready to move']['price'].mean()
utc_avg_price = df[df['status'] == 'under construction']['price'].mean()
if rtm_avg_price > utc_avg_price:
    print(f"Ready to move flats are more expensive on average")
else:    print(f"Under construction flats are more expensive on average")

# a = df[df['status'] == 'ready to move'].head(10)
# print(a)

#Q5 : Does RERA-approved properties command a price premium
rera_approved= df[df['rera_approval']==True]['price'].mean()
rera_not_approved = df[df['rera_approval']==False]['price'].mean()
if(rera_approved>rera_not_approved):
    print("Yes, RERA-approved properties commands a price premium")
else:
    print("No, RERA-approved properties doesn't command a price premium")

#Q6 : how does area(sqft) affect the price of flats?
# sns.scatterplot(x='area', y='price', data=df)
# plt.title('Area vs Price')
# plt.xlabel('Area (sqft)')
# plt.ylabel('Price')
# plt.savefig('area_vs_price.png')
# plt.show()

#Q7 : Which BHK configuration is the most expensive on average?
expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f"{expensive_bhk} BHK flats are the most expensive on average.")

# Q8 : Which property type (Apartment, Floor, Plot) is the costliest?
expensive_property = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print(f"{expensive_property} properties are the most expensive on average.")

# Q9 : Do certain builders or companies consistently price higher?
expensive_company = df.groupby(['company_name'])['rate_per_sqft'].mean().sort_values(ascending=False).head().round(2)
print("Top 10 most expensive companies based on rate per sqft:", end = ' ')
for company in expensive_company.index:
    print(company ,end = ', ')   
# print(expensive_company)


# Q10: Are larger homes always more expensive per square foot?

# sns.scatterplot(x='area', y='rate_per_sqft', data=df)
# plt.title('Area vs Rate per Sqft')
# plt.xlabel('Area (sqft)')
# plt.ylabel('Rate per Sqft')
# plt.savefig('area_vs_rate_per_sqft.png')
# plt.show()