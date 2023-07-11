def ara_bul(sayilar, hedef):
    # Eğer Değerimiz Sayilar Listesinde varsa indexini yazdırıyoruz.
    if hedef in sayilar:
        print(sayilar.index(hedef))
    # Listemizde yoksa yapılacaklar
    else:
        # Değeri Ekliyoruz
        sayilar.append(hedef)
        # Listeyi Yeniden sıralıyoruz
        sayilar.sort()
        # indexi yazdırıyoruz.
        print(sayilar.index(hedef))


ara_bul([1, 2, 4, 8], 4)
ara_bul([2, 4, 5, 8], 3)

# For ile yapilmiş Fonksiyon Tanımlıyoruz
def ara_bul(sayilar, hedef):
    # Eğer Değerimiz Sayilar Listesinde varsa indexini yazdırıyoruz.
    if hedef in sayilar:
        print(sayilar.index(hedef))
    # Listemizde yoksa yapılacaklar
    else:
        index = 0
        for sayi in sayilar:
            if sayi > hedef:
                sayilar.insert(index, hedef)
                print(index)
                break
            index += 1


sayilar = input("Sayıları girin (virgülle ayrılmış): ").split(",")
sayilar = [int(sayi) for sayi in sayilar]
hedef = int(input("Hedef sayıyı girin: "))

ara_bul(sayilar, hedef)
