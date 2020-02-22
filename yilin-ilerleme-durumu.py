# Yılın gününe göre ilerleme durumu
import datetime

# Ön tanımlamalar
suan = datetime.datetime.now()
yilin_gunu = float(suan.strftime("%j"))
yil2020 = float(366)

# Zaman, ilerleme ve şekil hesaplamaları
ilerleme_yuzdesi = (100 / yil2020) * (yilin_gunu) # İlerleme oranı
cizgi = (ilerleme_yuzdesi/2.5) # İlerleme alanı
p = "▊" * int(cizgi) # İlerleme simgesi

# Zaman aralığı bulma
g = datetime.datetime.strptime("31 12 2019", "%d %m %Y")
gecen = (suan-g).days

k = datetime.datetime.strptime("31 12 2020", "%d %m %Y")
kalan = (k-suan).days

# Ekran çıktısı
print("\n"*5)
print("Yıl: {} | Geçen gün: {} | Kalan gün: {}" .format(suan.year, gecen, kalan))
print("-"*52)
print("|{:<50}|%{}" .format(p, round(ilerleme_yuzdesi, 2)) .ljust(50))
print("-"*52)
print("\n"*2)