import cv2
import numpy as np # as np yazdığımızda numpy kütüphanesinin kısaltımı olarak alır.
# import ile cv2 ve np kütüphanelerini çağırdık

resim = cv2.imread("st.jpg") # st.jpg resmimizi imread ile resim değişkenine atadık

#resim[:,:,0]=255 # Resime B=0 ile blue atadık

#resim[:,:,1]=255 # Resime G=1 ile green atadık

#resim[:,:,2]=255 # Resime R=2 ile red atadık 

#resim[300:500,600:900,0]=255 # Belli bölüme mavi atadık
# Resmin belli bölümüne efekt uygular ilk kısım y ikinci kısım x

#resim[400:450,300:350]=(0,150,255) # Seçilen alana B = 0, G= 150 , R = 255 renginin karışımını ata

cv2.rectangle(resim,(50,100),(150,30),[0,0,255],9)
# sol alt ve sağ üstten sonraki renk ve en sondaki ise karenin kalınlığıdır.
# Sol alt ve sağ üst köşeler içerisinde kalan karenin ilk (x,y) sola alt sonraki sağ üst

cv2.imshow("Normal Resim",resim) # Resim değişkenimizi imshow ile çıktısını aldık

cv2.waitKey(0)
cv2.destroyAllWindows()

