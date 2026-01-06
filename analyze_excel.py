import pandas as pd

print("=" * 80)
print("ANALISIS FILE EXCEL UNTUK DASHBOARD AKUNTANSI")
print("=" * 80)

# 1. FILE INVOICE
print("\n" + "=" * 60)
print("1. FILE INVOICE")
print("=" * 60)
xl = pd.ExcelFile('file_invoice.xlsx')
print(f"Sheets: {xl.sheet_names}")
for sheet in xl.sheet_names[:2]:  # Batasi 2 sheet
    df = pd.read_excel(xl, sheet_name=sheet, header=None)
    print(f"\n>>> Sheet: {sheet}")
    print(f"Shape: {df.shape}")
    print(df.iloc[:15, :10].to_string())

# 2. PENGELUARAN
print("\n" + "=" * 60)
print("2. PENGELUARAN BULAN SEPTEMBER")
print("=" * 60)
xl = pd.ExcelFile('PENGELUARAN_BULAN_SEPTEMBER.xlsx')
print(f"Sheets: {xl.sheet_names}")
for sheet in xl.sheet_names[:3]:  # Batasi 3 sheet
    df = pd.read_excel(xl, sheet_name=sheet, header=None)
    print(f"\n>>> Sheet: {sheet}")
    print(f"Shape: {df.shape}")
    print(df.iloc[:15, :7].to_string())

# 3. FILE GAJI
print("\n" + "=" * 60)
print("3. FILE GAJI BMM CARGO")
print("=" * 60)
xl = pd.ExcelFile('FILE_GAJI_BMM_CARGO.xlsx')
print(f"Sheets: {xl.sheet_names}")
for sheet in xl.sheet_names:
    df = pd.read_excel(xl, sheet_name=sheet, header=None)
    print(f"\n>>> Sheet: {sheet}")
    print(f"Shape: {df.shape}")
    print(df.iloc[:25, :12].to_string())

# 4. LAPORAN RUGI LABA
print("\n" + "=" * 60)
print("4. LAPORAN RUGI LABA BMM")
print("=" * 60)
xl = pd.ExcelFile('LAPORAN_RUGI_LABA_BMM.xlsx')
print(f"Sheets: {xl.sheet_names}")
for sheet in xl.sheet_names:
    df = pd.read_excel(xl, sheet_name=sheet, header=None)
    print(f"\n>>> Sheet: {sheet}")
    print(f"Shape: {df.shape}")
    print(df.to_string())

print("\n" + "=" * 80)
print("SELESAI")
print("=" * 80)
