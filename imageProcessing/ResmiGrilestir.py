import cv2
import numpy as np # as np yazdığımızda numpy kütüphanesinin kısaltımı olarak alır.
# import ile cv2 ve np kütüphanelerini çağırdık

resim = cv2.imread("rsm.jpg") # st.jpg resmimizi imread ile resim değişkenine atadık

cv2.imshow("Normal Resim",resim) # Resim değişkenimizi imshow ile çıktısını aldık

resim1 = cv2.imread("rsm.jpg",0) # st.jpg,0 yazarak 0 ile resmi siyah beyaz konuma getirdik

cv2.imshow("Siyah Beyaz",resim1) # Resim değişkenimizi imshow ile çıktısını aldık

cv2.waitKey(0)
cv2.destroyAllWindows()