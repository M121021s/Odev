class Personel:
    def __init__(self, adı, departmanı, çalışma_yılı, maaşı):
        self.adı = adı                # Personelin adını tutar.
        self.departmanı = departmanı  # Personelin çalıştığı departmanı tutar.
        self.çalışma_yılı = çalışma_yılı  # Personelin şirkette çalıştığı yılı tutar.
        self.maaşı = maaşı            # Personelin maaşını tutar.

class Firma:
    def __init__(self):
        self.personel_listesi = []  # Firma içindeki personellerin listesini tutar.

    def personel_ekle(self, personel):
        # Firma içine yeni bir personel ekler.
        self.personel_listesi.append(personel)

    def personel_listele(self):
        # Firma içindeki tüm personellerin bilgilerini ekrana yazdırır.
        for personel in self.personel_listesi:
            print("Adı:", personel.adı)
            print("Departmanı:", personel.departmanı)
            print("Çalışma Yılı:", personel.çalışma_yılı)
            print("Maaşı:", personel.maaşı)
            print("--------------------------")

    def maaş_zammı(self, personel, zam_oranı):
        # Belirli bir personelin maaşına zam yapar.
        personel.maaşı *= (1 + zam_oranı / 100)

    def personel_çıkart(self, personel):
        # Firma içinden bir personeli çıkarır.
        self.personel_listesi.remove(personel)


if __name__ == "__main__":
    firma = Firma()

    personel1 = Personel("Ahmet", "Satış", 5, 5000)
    personel2 = Personel("Mehmet", "Pazarlama", 3, 4500)
    

    # Firma içine personelleri ekliyoruz
    firma.personel_ekle(personel1)
    firma.personel_ekle(personel2)

    print("Firma Çalışanları:")
    firma.personel_listele()  # Firma içindeki personelleri listeliyoruz

    print("\nMaaş zammı uygulanmadan önce:")
    firma.personel_listele()  # Maaş zammı uygulanmadan önceki durumu listeliyoruz

    firma.maaş_zammı(personel1, 10)  # Ahmet'in maaşına %10 zam yapıyoruz

    print("\nMaaş zammı uygulandıktan sonra:")
    firma.personel_listele()  # Maaş zammı uygulandıktan sonraki durumu listeliyoruz

    firma.personel_çıkart(personel2)  # Mehmet'i listeden çıkarıyoruz

    print("\nMehmet işten çıkarıldıktan sonra:")
    firma.personel_listele()  # Mehmet çıkarıldıktan sonraki durumu listeliyoruz
