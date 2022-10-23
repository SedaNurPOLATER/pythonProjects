# İlk olarak instaloader kütüphanesini pip install yaparak indiriyoruz ve ardında imort ederek projemizde kullanıyoruz
import instaloader

S = instaloader.Instaloader()
# Giriş yapılabilmesi için kullanıcı adı ve şifre yazılıyor
username = "Kullanıcı_adı"
password = "Şifre"
S.login(username, password)
profile = instaloader.Profile.from_username(S.context, username)

# ilk olarak takipçileri alıyoruz
for followers in profile.get_followers():
    with open("takipci.txt","a+") as f:
        file = f.write(followers.username+'\n')
        
    print("takipçiler yazılıyor...")
    print(file)
# Daha sonra takip edilenleri alıyoruz    
for followed in profile.get_followed():
    with open("takipedilen.txt","a+") as f:
        file = f.write(followed.username+'\n')
    print("takip edilenler yazılıyor....")
    print(file)
    
# Takipçileri ve takip edenleri yazdırarak aradaki farkı bulduruyoruz
followers_file = set(open("takipci.txt").readlines())
followed_file = set(open("takipedilen.txt").readlines())

unfollowers_set = followed_file.difference(followers_file)
# Farkı unfollowers_set e atayarak yazdırıyoruz
for unfollowers in unfollowers_set:
    print(unfollowers) # Sonuçta takip ettiğimiz fakat bizi takip etmeyen kullanıcıları bulabiliyoruz
