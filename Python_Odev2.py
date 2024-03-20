def is_letter(char):
    """
    Verilen karakterin bir harf olup olmadigini kontrol eder.
    """
    if char.isalpha():  # Eğer karakter bir harfse
        return True     # True değerini döndür
    else:
        return False    # Değilse False değerini döndür

def to_lowercase(char):
    """
    Verilen karakteri küçük harfe çevirir.
    """
    return char.lower()  # Karakteri küçük harfe çevirip döndür

def calculate_frequency(text):
    """
    Verilen metindeki harflerin kullanim sikligini yüzde olarak hesaplar.
    """
    frequency = {}      # Harf sıklıklarını tutacak bir sözlük oluştur
    total_chars = 0     # Toplam harf sayısını tutacak bir değişken oluştur

    for char in text:   # Metindeki her bir karakter için
        if char.isalpha():  # Eğer karakter bir harfse
            total_chars += 1    # Toplam harf sayısını bir artır
            if char in frequency:   # Eğer karakter sözlükte zaten varsa
                frequency[char] += 1    # Sayısını bir artır
            else:
                frequency[char] = 1     # Değilse, sözlüğe ekle ve sayısını 1 olarak ata
    
    # Harf kullanım sıklığını yüzde olarak hesapla
    frequency_percentage = {char: (count / total_chars) * 100 for char, count in frequency.items()}
    return frequency_percentage

def print_info():
    """
    Kendi bilgilerini ve notunu ekrana yazdirir.
    """
    print("Ad: Sukru")
    print("Soyad: Karagoz")
    print("Öğrenci Numarasi: 221213124")
    print("Not: Bu modül, harf işlemleri için tasarlanmistir.")

if __name__ == "__main__":
    text = input("Lütfen bir metin girin: ")

    # Her bir karakteri küçük harfe çevir ve ekrana yazdır
    for char in text:
        if is_letter(char):
            print(f"{char} -> {to_lowercase(char)}")

    # Harf kullanım sıklığını hesapla ve ekrana yazdır
    frequency = calculate_frequency(text)
    print("Harf Kullanim sikligi:")
    for char, percentage in frequency.items():
        print(f"{char}: %{percentage:.2f}")

    # Kişisel bilgileri ve notu ekrana yazdır
    print_info()
