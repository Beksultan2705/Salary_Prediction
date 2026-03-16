import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data from your CSV
# Make sure 'inflation_kg.csv' is in the same folder as this script
df_inf = pd.read_csv('inflation_kg.csv')

# 2. Setup style and figure size
plt.figure(figsize=(12, 6))
plt.style.use('seaborn-v0_8-muted')

# 3. Create Bar Chart
# Using 'steelblue' for a professional look
bars = plt.bar(df_inf['Year'], df_inf['Inflation'], color='steelblue', alpha=0.8)

# 4. Add data labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f'{yval}%',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

# 5. Formatting (English)
plt.title('Annual Inflation Rate in Kyrgyzstan (%)', fontsize=16, pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Inflation Rate (%)', fontsize=12)
plt.xticks(df_inf['Year'])  # Ensure every year is displayed
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 6. Add a reference line for high inflation (e.g., above 10%)
plt.axhline(y=10, color='red', linestyle='-', alpha=0.3, label='High Inflation Threshold (>10%)')
plt.legend()

plt.tight_layout()
plt.show()
