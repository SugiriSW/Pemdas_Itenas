import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Fungsi lambda untuk menghitung gaji setelah peningkatan 5%
hitung_gaji_setelah_peningkatan = lambda gaji: gaji * 1.05

# Fungsi lambda untuk menghitung gaji setelah peningkatan tambahan 2% untuk usia di atas 30 tahun
hitung_gaji_tambahan_usia = lambda gaji, usia: gaji * 1.02 if usia > 30 else gaji

# Tampilkan DataFrame sebelum perubahan
print("DataFrame sebelum perubahan:")
print(df)

# Gunakan loop for untuk mengiterasi setiap baris dan update kolom 'Gaji'
for index, row in df.iterrows():
    gaji_setelah_peningkatan = hitung_gaji_setelah_peningkatan(row['Gaji'])
    df.at[index, 'Gaji'] = hitung_gaji_tambahan_usia(gaji_setelah_peningkatan, row['Usia'])

# Tampilkan DataFrame setelah perubahan
print("\nDataFrame setelah perubahan:")
print(df)

# Ringkasan hasil
ringkasan = f"\nRingkasan hasil:\nGaji setelah perubahan:\n{df['Gaji'].tolist()}"
print(ringkasan)
