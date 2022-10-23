import cv2
import numpy as np # as np yazdığımızda numpy kütüphanesinin kısaltımı olarak alır.
# import ile cv2 ve np kütüphanelerini çağırdık

resim = cv2.imread("st.jpg") # st.jpg resmimizi imread ile resim değişkenine atadık

resim1 = cv2.imread("rsm.jpg") # rsm.jpg resmimizi imread ile resim değişkenine atadık

cv2.imshow("st Resim",resim) # Resim değişkenimizi imshow ile çıktısını aldık

cv2.imshow("rsm Resim",resim1) # Resim değişkenimizi imshow ile çıktısını aldık

print("Resim BGR Değeri", resim[100,200])
print("Resim1 BGR Değeri", resim1[300,430])
print("Yeni BGR Değeri:" , resim[100,200]+resim1[300,430])
# 2 resimin BGR değerlerini toplayıp yeni BGR değeri elde etme


cv2.waitKey(0)
cv2.destroyAllWindows()