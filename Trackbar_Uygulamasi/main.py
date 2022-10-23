#Kütüphaneleri atıyoruz
import cv2
import numpy as np

# Varsayılan olarak boş fonksiyon tanımlıyoruz
def nothing(x):
    pass

# Siyah tuval tanımladık
tüval = np.zeros((512, 512, 3), np.uint8)

# Fonksiyon ile Trackbar tuvalimize isim veriyoruz
cv2.namedWindow("Trackbar")

"""Tüvalimizdeki verilerin renkleri, hangi tüvalde görünecekleri, renk aralıklarını 
ve boş fonksiyonumuzu varsayılan olarak atayalım verelim"""
cv2.createTrackbar("Red", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Green", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Blue", "Trackbar", 0, 255, nothing)

# Anahtar kapalı ile renk ddeğişimi olmasın, açık olduğunda renk değişimi olsun diyelim
cv2.createTrackbar("Ac/Kapat", "Trackbar", 0, 1, nothing)

# Döngüye girelim ve ekranda tüvalimizi gösterelim
while (1):
    cv2.imshow("Trackbar", tüval)
# q ile döngüden çıkalım
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# R,G,B değerlerini çekelim
    r = cv2.getTrackbarPos("Red", "Trackbar")
    g = cv2.getTrackbarPos("Green", "Trackbar")
    b = cv2.getTrackbarPos("Blue", "Trackbar")
    key = cv2.getTrackbarPos("Ac/Kapat", "Trackbar")

# Eğer anahtar 1 ise yani açıksa b,g,r daki değerleri al ve tüvale ata
    if key == 1:
        tüval[:] = [b, g, r]
# Eğer anahtar 0 ise yani kapalıysa tüvale 0(siyah) değerini ata
    else:
        tüval[:] = 0

cv2.destroyAllWindows()

