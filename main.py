from menu import baslik_goster, menu_goster, kullanici_secimi
from ogrenci import ogrenci_ekle, ogrencileri_listele, ogrenci_ara, ogrenci_sil
from not_islemleri import not_ekle
from ortalama import ortalama_hesapla


baslik_goster()


while True:

    menu_goster()

    secim = kullanici_secimi()

    if secim == "1":
        ogrenci_ekle()

    elif secim == "2":
        ogrencileri_listele()

    elif secim == "3":
        not_ekle()

    elif secim == "4":
        ortalama_hesapla()

    elif secim == "5":
        ogrenci_ara()

    elif secim == "6":
        ogrenci_sil()

    elif secim == "7":
        print("Program kapatılıyor...")
        break

    else:
        print("Geçersiz seçim yaptınız.")