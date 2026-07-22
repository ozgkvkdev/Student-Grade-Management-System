from veriler import ogrenciler

def ogrenci_ekle():

    ad = input("Öğrenci Adı: ")
    soyad = input("Öğrenci Soyadı: ")
    numara = input("Öğrenci Numarası: ")

    ogrenci = {
        "ad": ad,
        "soyad": soyad,
        "numara": numara,
        "notlar": []
    }

    ogrenciler.append(ogrenci)

    print("Öğrenci Başarıyla Eklendi")

def ogrencileri_listele():
    if len(ogrenciler) == 0:
        print("Kayıtlı öğrenci yok.")
    else:
        for ogrenci in ogrenciler:
            print(f"Ad: {ogrenci['ad']}, Soyad: {ogrenci['soyad']}, Numara: {ogrenci['numara']}, Notlar: {ogrenci['notlar']}")