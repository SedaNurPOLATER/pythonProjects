import random
number = random.randint(1, 10)
#Kullanıcıya hitap edebilmek için kullanıcıdan isim istedik
player_name = input("Merhaba, ismin ne?")
number_of_guesses = 0
print('Tamam! '+ player_name+ ' 1 ile 10 arasında bir sayı tahmin et:')

# 5 deneme hakkı verildi
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Tahminin çok düşük')
    if guess > number:
        print('Tahminin çok yüksek')
    if guess == number:
        break
if guess == number:
    print(str(number_of_guesses) + '. denemede doğru tahmin ettin...')
else:
    print('Sayıyı tahmin edemedin. Sayı: ' + str(number))