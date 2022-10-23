
import cv2
import numpy as np # as np yazdığımızda numpy kütüphanesinin kısaltımı olarak alır.
# import ile cv2 ve np kütüphanelerini çağırdık

resim = cv2.imread("st.jpg") # st.jpg resmimizi imread ile resim değişkenine atadık

cv2.imshow("Normal Resim",resim) # Resim değişkenimizi imshow ile çıktısını aldık

aynalananResim = cv2.copyMakeBorder(resim,75,75,125,125,cv2.BORDER_REFLECT)
cv2.imshow("Aynalama", aynalananResim)

uzatilan=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE)
cv2.imshow("Uzatilan", uzatilan)

tekrar = cv2.copyMakeBorder(resim,300,300,300,300, cv2.BORDER_WRAP)
cv2.imshow("Tekrar", tekrar)

sarilan = cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT,value=(75,150,255))
cv2.imshow("Sarilan", sarilan)

cv2.waitKey(0)
cv2.destroyAllWindows()

