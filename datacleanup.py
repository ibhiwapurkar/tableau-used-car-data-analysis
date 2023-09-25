# importing pandas library to read and write CSV file
import pandas as pd

# reading the data using pd.read_csv function and then printing top 5 records
df = pd.read_csv('vehicles.csv', sep=',')
df.head()

# printing the columns in the dataframe
df.columns

# taking the subset of columns from the parent dataframe df and printing the top 5 records
df_cars = df[['region', 'price', 'year', 'manufacturer', 'model', 'fuel', 'odometer', 'title_status', \
              'transmission', 'type', 'state', 'lat', 'long', 'posting_date']]
df_cars.head()

# printing the number of records in the dataframe
len(df_cars)


# printing the % of null records per column in the dataframe
(df_cars.isnull().sum()/len(df_cars))*100


# removing the null records for each column in the dataframe
df_cars = df_cars.dropna(subset=['region', 'price', 'year', 'manufacturer', 'model', 'fuel', 'odometer', \
                                 'title_status', 'transmission', 'type', 'state', 'lat', 'long', 'posting_date'])

# removing the outliers
# removing prices greater than 100k
df_cars = df_cars[df_cars['price']<100000]
# removing car year older than 2000
df_cars = df_cars[df_cars['year']>=2000]
# removing car odometer greater than 300k
df_cars = df_cars[df_cars['odometer']<=300000]
# removing car odometer equal to 0
df_cars = df_cars[df_cars['odometer']>0]


# printing the number of records in the dataframe
len(df_cars)

# making sure there is no null records in the dataframe
(df_cars.isnull().sum()/len(df_cars))*100
