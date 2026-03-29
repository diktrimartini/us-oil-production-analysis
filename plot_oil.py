import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

#Load data
data = pd.read_csv("oil_production.csv")

# cek kolom
print(data.columns)
# rename kolom
data = data.rename(columns={"U.S. Field": "us_production"})

# ubah ke datetime
data['date'] = pd.to_datetime(data['date'])

# statistik
print(f"Rata-rata Produksi:, {data['us_production'].mean():,.2f}")
print(f"Produksi Tertinggi:, {data['us_production'].max():,.2f}")
print(f"Produksi Terendah:, {data['us_production'].min():,.2f}")

# plot
plt.figure(figsize=(10,5)) # ukuran lebih kecil
plt.plot(data['date'], data['us_production'], label='US')

plt.xlabel("Year")
plt.ylabel("Oil Production (Barrels)")
plt.title("US Crude oil Production Trend (1981-Present)")

# format angka pakai koma
plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
plt.legend()
plt.grid()

plt.savefig("oil_production.png")
plt.show()
