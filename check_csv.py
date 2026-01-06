import csv
import re

with open('kas_harian.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    rows = list(reader)

print(f'Total baris di CSV: {len(rows)}')
print(f'Data setelah header (4 baris): {len(rows) - 4}')

# Hitung baris yang valid vs skip
valid = 0
skip_empty_date = 0
skip_empty_nominal = 0
skip_zero_nominal = 0
skip_other = 0
skipped_rows = []

for i, row in enumerate(rows[4:], start=5):
    if len(row) < 4:
        skip_other += 1
        skipped_rows.append((i, 'kolom kurang', row[:4] if row else 'empty'))
        continue
    if not row[1].strip():
        skip_empty_date += 1
        skipped_rows.append((i, 'tanggal kosong', row[:4]))
        continue
    if not row[3].strip():
        skip_empty_nominal += 1
        skipped_rows.append((i, 'nominal kosong', row[:4]))
        continue
    
    # Check nominal
    nominal_str = re.sub(r'[Rp\s,.]', '', row[3].strip())
    if not nominal_str or nominal_str == '-' or nominal_str == '0':
        skip_zero_nominal += 1
        skipped_rows.append((i, 'nominal 0 atau invalid', row[:4]))
        continue
    valid += 1

print(f'\n=== HASIL ANALISIS ===')
print(f'Baris valid: {valid}')
print(f'Skip tanggal kosong: {skip_empty_date}')
print(f'Skip nominal kosong: {skip_empty_nominal}')
print(f'Skip nominal 0/invalid: {skip_zero_nominal}')
print(f'Skip lainnya: {skip_other}')
print(f'Total skip: {skip_empty_date + skip_empty_nominal + skip_zero_nominal + skip_other}')

print(f'\n=== BARIS YANG DISKIP (sample) ===')
for row in skipped_rows[:20]:
    print(row)
