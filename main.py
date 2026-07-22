from menu import baslik_goster,menu_goster,kullanici_secimi
from ogrenci import ogrenci_ekle,ogrencileri_listele

baslik_goster()
menu_goster()

secim=kullanici_secimi()
print(f"Seçiminiz: {secim}")

while True:
    menu_goster()

    secim = kullanici_secimi()

    if secim == "1":
        ogrenci_ekle()

    elif secim == "2":
        ogrencileri_listele()

    elif secim == "7":
        print("Program kapatılıyor...")
        break