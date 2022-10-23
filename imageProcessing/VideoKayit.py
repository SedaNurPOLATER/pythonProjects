import cv2 # cv2 kütüphanesini import ettik.

camera = cv2.VideoCapture(0) # cv2 den video kayıt özelliğini camera değişkenine atadık
# 0 yazdığımız için cihazın kamerasına ulaşıyoruz.

width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)) # Framein Genişlik değeri
height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Framein Yükseklik değeri

print(width,height) # Yükseklik ve genişliği terminalde yazdırdık

fourcc = cv2.VideoWriter_fourcc(*'MP4V') # 4 karakterli kodu burada tanımladık ve mp4 şeklinde atadık

writer =cv2.VideoWriter("kayit.mp4",fourcc,20,(width,height)) # Videomuzu yazdırıyor, 3. parametrede saniyelik görüntü sayısını belirleriz.

while True: # Döngüye girerek görüntüyü almasını sağladık
    ret,frame = camera.read() # Kamera değişkenini okuyoruz
    writer.write(frame) # Writer değişkeninin içine framei yazdırıyoruz.
    cv2.imshow("Kayit videosu",frame) # Kayıt videosunu kullanıcıya verir
    
    if cv2.waitKey(25) & 0xFF == ord("q"): # 25 milisaniyede bir görüntüyü alır, q ile kayıt biter ve çıkılır.
        break # q ya basınca çıkmayı sağlar.
    
camera.release()
writer.release()
cv2.destroyAllWindows() # Tüm pencereleri kapatır.

