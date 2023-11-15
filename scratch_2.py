
import pandas as pd


data = pd.DataFrame({
    "Demand (in millions)": [2, 7, 10, 12, 14, 20, 30],
    "Price (in dollars)": [1563, 1783, 1852, 1930, 3700, 4300, 5350]
})
print(data)


data["% Change in Demand"] = data["Demand (in millions)"].pct_change()
data["% Change in Price"] = data["Price (in dollars)"].pct_change()
print(data)

# Calculating Price Elasticity using the correct columns for percentage changes
data["Price Elasticity"] = data["% Change in Demand"] / data["% Change in Price"]
print(data)

