import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('Cleaned_Zameen.csv')



# # Filter only House listings (case-insensitive)
# houses_df = df[df["property_type"].str.contains("house", case=False, na=False)]

# # Count houses per city
# city_counts = houses_df["city"].value_counts().head(10)

# # Plot bar chart
# plt.figure(figsize=(10, 5))
# plt.bar(city_counts.index, city_counts.values)
# plt.xlabel("City")
# plt.ylabel("Number of Houses Available")
# plt.title("Top 10 Cities with Houses Available")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()




# #1st graph: Grouped Bar Chart of House Types Across Cities
# Keep only required house types
house_types = [
    "Flat",
    "Penthouse",
    "House",
    "Lower Portion",
    "Upper Portion"
]

df = df[df['property_type'].isin(house_types)]

# Create pivot table
pivot_df = pd.pivot_table(
    df,
    index='city',
    columns='property_type',
    aggfunc='size',
    fill_value=0
)

# Plot grouped bar chart
pivot_df.plot(
    kind='bar',
    figsize=(12,6)
)
plt.grid(axis='y')
plt.xlabel("City Names")
plt.ylabel("Number of Houses")
plt.title("Availability of House Types Across Cities")
plt.xticks(rotation=0)
plt.legend(title="House Type")
plt.tight_layout()
# plt.show()

#2nd graph: Heatmap of House Availability
import seaborn as sns

# Calculate listing count
availability = (
    df.groupby(['city', 'property_type'])
    .size()
    .reset_index(name='Listing Count')
)

# Pivot for stacked bar chart
pivot_df = availability.pivot(
    index='city',
    columns='property_type',
    values='Listing Count'
)

# Plot stacked bar chart
plt.figure(figsize=(13, 6))
pivot_df.plot(kind='bar', stacked=True)

plt.title('Property Availability Across Cities by Property Type')
plt.xlabel('City')
plt.ylabel('Number of Listings')
plt.xticks(rotation=45)
plt.legend(title='Property Type', bbox_to_anchor=(1.05, 1))
plt.tight_layout()

#3rd graph: Price Intensity Heatmap

house_types = [
    "Flat",
    "Penthouse",
    "House",
    "Lower Portion",
    "Upper Portion"
]

df = df[df['property_type'].isin(house_types)]

price_pivot = pd.pivot_table(
    df,
    index='city',
    columns='property_type',
    values='price',
    aggfunc='mean'
)

# 🔹 Convert to Millions
price_pivot = price_pivot / 1_000_000

plt.figure(figsize=(10,6))
sns.heatmap(
    price_pivot,
    annot=True,
    fmt=".2f",
    cmap="YlOrRd"
)

plt.title("Average Property Price (Million PKR)")
plt.xlabel("Property Type")
plt.ylabel("City")
plt.tight_layout()

#new cart
import matplotlib.pyplot as plt

# Count property types
property_counts = df['property_type'].value_counts()

# Plot bar chart
plt.figure(figsize=(8,5))
plt.bar(property_counts.index, property_counts.values)
plt.xlabel("Property Type")
plt.ylabel("Number of Listings")
plt.title("Overall Property Type Distribution")
plt.xticks(rotation=0)
plt.tight_layout()

#new graph
df = df[df['price'] > 0]

# Aggregate: Availability & Average Price by property type
summary = (
    df.groupby('property_type')
    .agg(
        Availability=('property_type', 'count'),
        Average_Price=('price', 'mean')
    )
    .reset_index()
)

# Create bubble chart
plt.figure(figsize=(10, 6))
plt.scatter(
    summary['Availability'],
    summary['Average_Price'],
    s=summary['Availability'] / 8,
    alpha=0.6
)

# Add labels
for _, row in summary.iterrows():
    plt.text(
        row['Availability'],
        row['Average_Price'],
        row['property_type'],
        fontsize=9,
        ha='center',
        va='center'
    )

plt.title('Average Property Price vs Availability by Property Type')
plt.xlabel('Number of Listings (Availability)')
plt.ylabel('Average Price (PKR)')
plt.tight_layout()
plt.show()


