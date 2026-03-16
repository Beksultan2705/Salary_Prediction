import matplotlib.pyplot as plt
import pandas as pd

file_path = "/Users/diushaliev_beksultan/Downloads/Telegram Desktop/dc.xlsx"
df_raw = pd.read_excel(file_path, skiprows=4)

print("Columns:", df_raw.columns.tolist())

years = [2020, 2021, 2022, 2023, 2024]

available_years = [col for col in df_raw.columns if col in years or str(col) in [str(y) for y in years]]
cols = ['Items'] + available_years

df_clean = df_raw[cols].dropna(subset=['Items'])

df = df_clean.set_index('Items').transpose()
df.index = df.index.astype(str) 
df.index.name = 'Year'


plt.style.use('seaborn-v0_8-muted')
fig, ax = plt.subplots(figsize=(14, 8))

for column in df.columns:
    region_name = str(column).strip()

    # Делаем линию всей республики жирной
    is_main = "Kyrgyz Republic" in region_name
    linewidth = 4 if is_main else 1.5
    alpha = 1 if is_main else 0.6

    ax.plot(df.index, df[column], marker='o', label=region_name,
            linewidth=linewidth, alpha=alpha)

plt.title('Average Monthly Salary in Kyrgyzstan (2020-2025)', fontsize=16, pad=20)
plt.ylabel('KGS (Soms)', fontsize=12)
plt.xlabel('Year', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Regions", fontsize=9)

for column in df.columns:
    last_val = df[column].iloc[-1]
    if pd.notnull(last_val):
        plt.text(len(df)-0.9, last_val, f'{int(last_val)}', va='center', fontsize=9)

plt.tight_layout()
plt.show()
