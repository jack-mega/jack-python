import pygame, random, sys

secret = random.randint(1, 99)
guess = 0
tries = 0


pygame.init()
screen = pygame.display.set_mode([640, 480])
pygame.time.delay(1000)
pygame.mixer.init()

ahoy = pygame.mixer.Sound("Ahoy.wav")
ahoy.set_volume(0.50)
toolow = pygame.mixer.Sound("TooLow.wav")
toolow.set_volume(0.50)
toohigh = pygame.mixer.Sound("TooHigh.wav")
toohigh.set_volume(0.50)
whatsyerguess = pygame.mixer.Sound("WhatsYerGuess.wav")
whatsyerguess.set_volume(0.50)
avastgotit = pygame.mixer.Sound("AvastGotIt.wav")
avastgotit.set_volume(0.50)
nomore = pygame.mixer.Sound("NoMore.wav")
nomore.set_volume(0.50)



ahoy.play()
print "AHOY!  I'm the Dread Pirate Roberts, and I have a secret!"
print "It is a number from 1 to 99.  I'll give you 6 tries. "
pygame.time.delay(8000)


while guess != secret and tries < 6:
    pygame.time.delay(2000)
    whatsyerguess.play()
    guess = input("What's yer guess? ")
    if guess < secret:
        toolow.play()
        print "Too low, ye scurvy dog!"
    elif guess > secret:
        toohigh.play()
        print "Too high, landlubber!"
    tries = tries + 1


if guess == secret:
    avastgotit.play()
    print "Avast! Ye got it!  Found my secret, ye did!"
else:
    nomore.play()
    print "No more guesses!  Better luck next time, matey!"
    print "The secret number was", secret
