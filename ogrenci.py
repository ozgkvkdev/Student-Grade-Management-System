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


def ogrenci_ara():
    aranacak = input("Aranan Öğrenci Adı/Soyadı: ")
    bulundu = False
    
    for ogrenci in ogrenciler:
        if aranacak.lower() in ogrenci['ad'].lower() or aranacak.lower() in ogrenci['soyad'].lower():
            print(f"Adı: {ogrenci['ad']} {ogrenci['soyad']}, Numarası: {ogrenci['numara']}, Notları: {ogrenci['notlar']}")
            bulundu = True
    
    if not bulundu:
        print("Aranan öğrenci bulunamadı.")


def ogrenci_sil():
    no = input("Silinecek Öğrenci Numarası: ")
    bulundu = False
    
    for ogrenci in ogrenciler:
        if ogrenci['numara'] == no:
            ogrenciler.remove(ogrenci)
            print("Öğrenci başarıyla silindi.")
            bulundu = True
            break
    
    if not bulundu:
        print("Öğrenci bulunamadı.")
    