import cv2
import numpy as np # as np yazdığımızda numpy kütüphanesinin kısaltımı olarak alır.
# import ile cv2 ve np kütüphanelerini çağırdık

resim = cv2.imread("st.jpg") # st.jpg resmimizi imread ile resim değişkenine atadık

cv2.imshow("st Resim",resim) # Resim değişkenimizi imshow ile çıktısını aldık

ikiKatBuyuk=cv2.pyrUp(resim)
cv2.imshow("2 kat buyumus resim", ikiKatBuyuk)
# Orijinal resimi 2 kat büyütür.

ikiKatKucuk=cv2.pyrDown(resim)
cv2.imshow("2 kat kuculmus resim", ikiKatKucuk)
# Orijinal resimi 2 kat büyütür.

cv2.waitKey(0)
cv2.destroyAllWindows()

