# main.py

import Python_Odev2

text = input("Lütfen bir metin girin: ")

# Her bir karakteri küçük harfe çevir ve ekrana yazdır
for char in text:
    if Python_Odev2.is_letter(char):
        print(f"{char} -> {Python_Odev2.to_lowercase(char)}")

# Harf kullanım sıklığını hesapla ve ekrana yazdır
frequency = Python_Odev2.calculate_frequency(text)
print("Harf Kullanım Sıklığı:")
for char, percentage in frequency.items():
    print(f"{char}: %{percentage:.2f}")

# Kişisel bilgileri ve notu ekrana yazdır
Python_Odev2.print_info()
