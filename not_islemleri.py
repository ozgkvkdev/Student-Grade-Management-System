from veriler import ogrenciler

def not_ekle():
    no = input("Öğrenci Numarasını Giriniz: ")
    bulundu = False
    
    for ogrenci in ogrenciler:
        if ogrenci['numara'] == no:
            bulundu = True
            print("Öğrenci Bulundu")
            
            try:
                puan = input("Notunuzu Giriniz: ")
                ogrenci['notlar'].append(int(puan))
                print("Not Başarıyla Eklendi.")
            except ValueError:
                print("Lütfen geçerli bir sayı giriniz.")
            break
    
    if not bulundu:
        print("Öğrenci Bulunamadı.")
        

