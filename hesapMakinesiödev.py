print("""Hesap Makinesi
1 - Topla
2 - Çıkar
3 - Çarp
4 - Böl
5- Üs al
6- Tam Bölümü
7- Bölümünden Kalan
""")
islem = int(input("Yapılacak İşlemi Seçiniz:"))
sayi1 = int(input("1. Sayıyı Giriniz:"))
sayi2 = int(input("2. Sayıyı Giriniz:"))

if islem == 1 :
    print("Toplamı", int(sayi1 + sayi2))

elif islem == 2 :
    print("Farkı", int(sayi1 - sayi2))

elif islem == 3 :
    print("Çarpımı", int(sayi1 * sayi2))

elif islem == 4 :
    print("Bölümü:", int(sayi1 / sayi2))

elif islem == 5 :
    print("Üssü:", int(sayi1 ** sayi2))

elif islem == 6 :
    print("Tam Bölümü:", int(sayi1 // sayi2))

elif islem == 7 :
    print("Tam Bölümünden Kalan:", int(sayi1 % sayi2))
else:
    print("Sonuca Ulaştınız")