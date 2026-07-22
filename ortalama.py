from veriler import ogrenciler

def ortalama_hesapla():
    no = input("Öğrenci Numarasını Giriniz: ")
    bulundu = False
    
    for ogrenci in ogrenciler:
        if ogrenci['numara'] == no:
            bulundu = True
            
            if len(ogrenci['notlar']) == 0:
                print("Öğrencinin henüz notu yok.")
            else:
                ort = sum(ogrenci['notlar']) / len(ogrenci['notlar'])
                print(f"Öğrenci Ortalaması: {ort:.2f}")
            break
    
    if not bulundu:
        print("Öğrenci Bulunamadı.")