import sqlite3


baglan=sqlite3.connect('metin.db')

imlec=baglan.cursor()

#oluştur
imlec.execute('''CREATE TABLE IF NOT EXISTS metinler ( id INTEGER PRIMARY KEY, metin TEXT)''')

metin1 = input("İlk metin dosyasini giriniz: ")
metin2 = input("İkinci metin dosyasini giriniz: ")


# vt ekle
imlec.execute("INSERT INTO metinler (metin) VALUES (?)", (metin1,))
imlec.execute("INSERT INTO metinler (metin) VALUES (?)", (metin2,))

print("Metinler veritabanina eklendi")

baglan.commit()

baglan.close


def benzerlik_orani(metin1, metin2):
    uzunluk = max(len(metin1.split()), len(metin2.split()))
    eslesen_harf_sayisi = 0
    kelimeler1=metin1.split()
    kelimeler2=metin2.split()
    for a, b in zip(kelimeler1, kelimeler2):
        if a == b:
            eslesen_harf_sayisi += 1

    return eslesen_harf_sayisi / uzunluk *100 if uzunluk != 0 else 0



def main():
    oran = benzerlik_orani(metin1, metin2)

    print("İki metnin benzerlikleri oranı :%",oran)
  
if __name__ == "__main__":
    main()