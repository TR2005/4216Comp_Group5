import csv
import pgeocode
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as mpatches
import pandas as pd






def load_dataset():
    return pd.read_csv("USA Housing Dataset.csv")#


housing_prices = load_dataset()

    
housing_prices = pd.read_csv("USA Housing Dataset.csv")
housing_prices_df = pd.DataFrame(housing_prices)
#determine duplicates and also their respective averages 
bath_duplicates = housing_prices_df['bathrooms'][housing_prices_df['bathrooms'].duplicated(keep=False)]
duplicates = housing_prices_df['yr_renovated'][housing_prices_df['yr_renovated'].duplicated(keep=False)]
bath_avg_prices = housing_prices_df[housing_prices_df['bathrooms'].isin(bath_duplicates)].groupby('bathrooms')['price'].mean()
avg_prices = housing_prices_df[housing_prices_df['yr_renovated'].isin(duplicates)].groupby('yr_renovated')['price'].mean()
    #define both methods of replacing the duplicated rows
def replace_with_avg_price(product, price):
        if product in avg_prices:
            return avg_prices[product]
        else:
            return price 
def replace_with_bath_avg_price(product, price):
        if product in bath_avg_prices:
            return bath_avg_prices[product]
        else:
            return price
    #using the previous functions to put the averages back into the correct rows and then getting the needed data out of the datafrane
housing_prices_df['price'] = housing_prices_df.apply(lambda row: replace_with_avg_price(row['yr_renovated'], row['price']), axis=1)
housing_prices_df.sort_values(by='yr_renovated')
ren_housing_prices = housing_prices_df.sort_values(by='yr_renovated')[housing_prices_df.sort_values(by='yr_renovated')["yr_renovated"]>0]
price_housing_prices = ren_housing_prices["price"]
yrren_housing_prices = ren_housing_prices["yr_renovated"]
#same as previous block but for the other visualisation data 
housing_prices_df['price'] = housing_prices_df.apply(lambda row: replace_with_bath_avg_price(row['bathrooms'], row['price']), axis=1)
housing_prices_df.sort_values(by='bathrooms')
bath_housing_prices = housing_prices_df.sort_values(by='bathrooms')[housing_prices_df.sort_values(by='bathrooms')["bathrooms"]>0]
bath_price = bath_housing_prices["price"]
bathrooms_housing_prices = bath_housing_prices["bathrooms"]

    #plotting the first visualisation 
fig, ax = plt.subplots()
fig.suptitle("Price to year renovated", fontsize=16)
ax.set_xlabel("Year renovated", fontsize=12)
ax.set_ylabel("Price (Millions)", fontsize=12)
ax.plot(yrren_housing_prices,price_housing_prices)
ax.grid(True)
plt.show()
#plotting the second visualisation 
fig, ax = plt.subplots()
fig.suptitle("Price to bathrooms", fontsize=16)
ax.set_xlabel("Bathrooms", fontsize=12)
ax.set_ylabel("Price (Millions)", fontsize=12)
ax.plot(bathrooms_housing_prices, bath_price)
ax.grid(True)
plt.show()

