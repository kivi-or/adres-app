import csv

# slownik = dict()
slownik_wejsciowy = 'slownik.csv'
plik_dane_in = 'plik_wej.csv'
plik_dane_out = 'plik_wyjs.csv'

#funkcja wczytujaca slownik z pliku csv
def wgranie_slownika(plik_wejsciowy, kolumna_ulicy, kolumna_kodu):
    slownik = dict()
    with open(plik_wejsciowy, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            slownik[row[kolumna_ulicy]]=row[kolumna_kodu]
    return slownik

def dopisanie_ulicy(ulica, slownik_wejsciowy):
    with open(slownik_wejsciowy, 'a', newline='', encoding='utf-8') as slownik:
        writer = csv.writer(slownik, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL )
        kod = input('podaj kod teryt: ')
        writer.writerow([ulica, kod])
#funkcja informujaca o braku ulicy w slowniku
def nie_ma_ulicy(ulica, slownik_wejsciowy):
    plik_z_blendami = 'error-file.csv'
    with open(plik_z_blendami, 'a', newline='', encoding='utf-8') as blad_file:
        writer = csv.writer(blad_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([ulica])
        dopisanie_ulicy(ulica, slownik_wejsciowy)

#funkcja pobierajaca dane z pliku csv zamieniajaca nazwe ulicy w kod i zapisujacy jako csv
def dopisywanie(plik_wej, plik_wyjs, slownik_wejsciowy):
    with open(plik_wej, 'r', newline='', encoding='utf-8') as plik_dane_wej, open(plik_wyjs, 'w', newline='', encoding='utf-8') as plik_dane_wyj:
        reader = csv.reader(plik_dane_wej)
        writer = csv.writer(plik_dane_wyj)
        for row in reader:
            ulica = row[0]
            dana = row[1]
            try:
                kod = slownik[ulica]
            except KeyError:
                print(f"nie_ma_ulicy {ulica} adres ten zostanie zapisany w pliku error")
                nie_ma_ulicy(ulica, slownik_wejsciowy)
                dopisanie_ulicy(ulica, slownik_wejsciowy)
            else:
                row.append(kod)
                writer.writerow(row)
                

slownik = wgranie_slownika(slownik_wejsciowy,1,0)
print(slownik)
dane = dopisywanie(plik_dane_in, plik_dane_out, slownik_wejsciowy)