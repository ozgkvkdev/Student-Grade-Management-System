from veriler import ogrenciler

def ogrenci_ekle():

    ad = input("Öğrenci Adı:")
    soyad = input("Öğrenci Soyadı:")
    numara = input("Öğrenci Numarası:")

    ogrenci={
        "ad":ad,
        "soyad":soyad,
        "numara":numara,
    }

    ogrenciler.append(ogrenci)
    print("Öğrenci Başarıyla Eklendi")
 