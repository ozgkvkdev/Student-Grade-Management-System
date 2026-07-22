from veriler import ogrenciler

def ortalama_hesapla():
    ogrenci_no = input("Öğrenci Numarasını Giriniz: ")
    bulundu = False
    for ogrenci in ogrenciler:
        if ogrenci['numara'] == ogrenci_no:
            bulundu = True
            if len(ogrenci['notlar']) == 0:
                print("Öğrencinin notu yok.")
            else:
                ortalama = sum(ogrenci['notlar']) / len(ogrenci['notlar'])
                print(f"Öğrenci Ortalaması: {ortalama:.2f}")
            break
    if not bulundu:
        print("Öğrenci Bulunamadı.")