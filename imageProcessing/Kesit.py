import cv2
import numpy as np # as np yazdığımızda numpy kütüphanesinin kısaltımı olarak alır.
# import ile cv2 ve np kütüphanelerini çağırdık

resim = cv2.imread("rsm.jpg")
# st.jpg resmimizi imread ile resim değişkenine atadık
cv2.imshow("Normal Resim",resim)
# Resim değişkenimizi imshow ile çıktısını aldık

kesit= resim[50:150,300:400]
cv2.imshow("kesit alani", kesit)
# Resimden y için 50:150 x için 300:400 alanını yeni resim olarak al

resim[0:100,0:100]=kesit
# Kesit olarak gelen yeni resim orjinal resimde 100 e 100 lük alana yapışır.
# Görmek için tekrar cv2.imshow("Normal Resim",resim) çağırılır.
cv2.imshow("Kesit yapıştı",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()