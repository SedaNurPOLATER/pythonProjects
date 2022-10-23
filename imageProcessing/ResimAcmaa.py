import cv2
import numpy as np # as np yazdığımızda numpy kütüphanesinin kısaltımı olarak alır.
# import ile cv2 ve np kütüphanelerini çağırdık

resim = cv2.imread("st.jpg") # st.jpg resmimizi imread ile resim değişkenine atadık

cv2.imshow("Normal Resim",resim) # Resim değişkenimizi imshow ile çıktısını aldık



print("Matrisler:" , resim) # st.jpg resminin matrislerini alır.

print("Resim boyutu:", resim.size) # Resmimizin boyutunu alıyoruz.

print("Resim veri tipi:" , resim.dtype) # Resmin veri tipini verir.

print("Resim genişlik, yükseklik, kanal sayısı:" , resim.shape) # resmin genişlik, yükseklik ve kanal sayısını verir

print("Y de 20, X de 30 olan renk kodları:", resim[(20,30)]) # BGR(BlueGreenRed) değerini verir y ekseninde 20, x ekseninde 30 ölçülerindeki renk kodları

cv2.waitKey(0)
cv2.destroyAllWindows()