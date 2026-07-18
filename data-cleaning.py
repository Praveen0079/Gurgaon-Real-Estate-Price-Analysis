import pandas as pd

df = pd.read_csv('data.csv')

# cleaning
# print(len(df))
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
df = df.drop_duplicates()
# print(len(df))

# Numerical data cleaning
df['price'] = df['price'].str.replace(',','').astype(int)
df['rate_per_sqft'] = df['rate_per_sqft'].str.replace(',','').astype(float)

# categorical data cleaning
cols_to_clean = ['status', 'property_type', 'builder_name','locality', 'socity', 'company_name', 'flat_type']
for x in cols_to_clean:
    df[x] = df[x].str.strip().str.lower()
# outliars
df = df.dropna(subset=['bhk_count','price'])
df = df.query('bhk_count<=7')

# print(len(df))
print(df.head(10))

