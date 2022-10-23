import cv2
import numpy as np # as np yazdığımızda numpy kütüphanesinin kısaltımı olarak alır.
# import ile cv2 ve np kütüphanelerini çağırdık

resim = cv2.imread("rsm.jpg") # st.jpg resmimizi imread ile resim değişkenine atadık

resim[50,30] = [255,255,255] # Resimde y ekseninden 50, x ekseninde 30 birim gidilen noktayı beyaza boya

cv2.imshow("Tek beyaz Nokta",resim) # Resim değişkenimizi imshow ile çıktısını aldık

resim1 = cv2.imread("rsm.jpg") # st.jpg resmimizi imread ile resim değişkenine atadık

for i in range(100):
    resim1[70,i]=[255,255,255] # Y de 100 birim aşağı inip x de 0 dan 100 e kadar her birimi beyaza boyar

cv2.imshow("Beyaz cizgi",resim1) # Resim değişkenimizi imshow ile çıktısını aldık

cv2.waitKey(0)
cv2.destroyAllWindows()
