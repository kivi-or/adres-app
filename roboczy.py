import csv
ulica = 'adam'
print(ulica)
plik_z_blendami = 'error-file.csv'
print(f"w bazie nie ma {ulica}")
with open(plik_z_blendami, 'w', encoding='utf-8') as blad_file:
    writer = csv.writer(blad_file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([ulica])