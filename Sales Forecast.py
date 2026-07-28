#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Sales Data Stimulation and Forecasting
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


np.random.seed(42) #To make random results reproducible- same number will be produced


# In[14]:


#Next step I will create sample sales Data
#Monthly sales for 5 products
#Revenue in Thousands

products=np.array([
    "Sugar",
    "Unga",
    "Cooking Oil",
    "lotion",
    "Salt"
])

sales=np.array([100,300,250,455,800])

print("Current Sales")
print("="*40)

for i in range(len(products)):
    print(f"{products[i]}:{sales[i]}")
    
#Next step I will add the market Variation
#Stumulation real-world changes:
#Random percentages between -15% and +15%

market_change=np.random.uniform(-0.15,0.15,len(sales))

#I will now adjust the sales after the variation

adjusted_sales=sales+(sales*market_change)

print("\nSales After Market Fluctuation")
print("="*40)

for i in range(len(products)):
    print(f"{products[i]}:{adjusted_sales[i]:.2f}")
    
#next step will involve forecasting next month sales

growth_rate=0.10

forecast_sales=adjusted_sales *(1+growth_rate)
print("\nForecasted Next Month Sales")
print("="*40)

for i in range(len(products)):
    print(f"{products[i]}:{forecast_sales[i]:.2f}")
    
#Now I will carry out the statistical Analysis

mean_sales=np.mean(adjusted_sales)
max_sales=np.max(adjusted_sales)
min_sales=np.min(adjusted_sales)
std_sales=np.std(adjusted_sales)
total_sales=np.sum(adjusted_sales)

print("n\Sales Statistics")
print("*"*50)

print(f"Average Sales:{mean_sales:.2f}")
print(f"Highest Sales:{max_sales:.2f}")
print(f"Lowest Sales:{min_sales:.2f}")
print(f"Standard Deviation:{std_sales:.2f}")
print(f"Total Sales:{total_sales:.2f}")
      
#I will now display the results
      
print("\nSales Summary")
print("="*60)

print("Product      current    adjusted    Forecast")

print("="* 60)
      
for i in range(len(products)):
      print(f"{products[i]:10} {sales[i]:8.0f}" 
            f"{adjusted_sales[i]:12.2f}"
            f"{forecast_sales[i]:12.2f}")
      


# In[ ]:




