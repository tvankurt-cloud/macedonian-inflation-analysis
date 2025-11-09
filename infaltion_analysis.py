# Data sources: 
# https://www.imf.org/en/Publications/selected-issues-papers/Issues/2025/05/22/Impact-of-International-Shocks-on-North-Macedonia-and-the-Western-Balkans-Republic-of-North-567136
import pandas as pd

# Example data structure
data = {
    'Year': [2016, 2017, 2018, 2019, 2026],
    'Inflation Rate (%)': [0.2, 1.4, 1.5, 0.8, 1.2]
}

df = pd.DataFrame(data)
print(df)

# Data visualization (e.g., using matplotlib or seaborn) can be added here
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['Inflation Rate (%)'], marker='o')
plt.title('Inflation Rate in North Macedonia (2012-2026)')
plt.xlabel('Year')
plt.ylabel('Inflation Rate (%)')
plt.grid()
plt.show()

avg_inflation = df['Inflation Rate (%)'].mean()
print(f"Average Inflation (2016–2020): {avg_inflation:.2f}%")

plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Inflation Rate (%)'], marker='o', linestyle='-', color='blue')
plt.axvline(x=2020.5, color='gray', linestyle='--', label='Projection Start')
plt.title('North Macedonia Inflation Rate (2016–2030)')
plt.xlabel('Year')
plt.ylabel('Inflation Rate (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()