import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample Data
data = {
    'year': [2020, 2020, 2020, 2021, 2021, 2022, 2022, 2022],
    'placed_students': [120, 150, 100, 180, 200, 130, 170, 160]
}

df = pd.DataFrame(data)

# Group by year and calculate mean, min, max
result = df.groupby('year')['placed_students'].agg(['mean', 'min', 'max']).reset_index()
print(result)

# Plot grouped bar chart
x = np.arange(len(result['year']))  # positions for years
width = 0.25  # bar width

plt.figure(figsize=(8, 5))

plt.bar(x - width, result['mean'], width, label='Mean')
plt.bar(x, result['min'], width, label='Min')
plt.bar(x + width, result['max'], width, label='Max')

plt.xticks(x, result['year'])
plt.xlabel("Year")
plt.ylabel("Placed Students")
plt.title("Placed Students (Mean, Min, Max) per Year")
plt.legend()
plt.show()
