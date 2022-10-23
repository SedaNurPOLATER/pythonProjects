import cv2
import numpy as np

resim= np.zeros((300,500,3),dtype="uint8")

cv2.line(resim,(50,50),(100,100),(20,60,255),3)

cv2.circle(resim,(150,150),25,(0,255,0),2)

cv2.putText(resim,"Seda Nur POLATER",(100,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)

cv2.imshow("Cikti", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()

