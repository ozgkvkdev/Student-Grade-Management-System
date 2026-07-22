from veriler import ogrenciler

def not_ekle():
    ogrenci_no=input("Öğrenci Numarasını Giriniz: ")
    bulundu=False
    for ogrenci in ogrenciler:
        if ogrenci['numara'] == ogrenci_no:
            bulundu=True
            print("Öğrenci Bulundu")
            try:
                not_degeri=input("Notunuzu Giriniz: ")
                ogrenci['notlar'].append(int(not_degeri))
                print("Not Başarıyla Eklendi.")
            except ValueError:
                print("Hata: Geçerli bir sayı giriniz.")
            break
    if not bulundu:
        print("Öğrenci Bulunamadı.")
        

