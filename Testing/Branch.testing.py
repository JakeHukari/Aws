import random
import os
import tweepy
from tweepy import lib

os.system('cls')

main = int(input("Enter a number: "))
deloc = int(random.randint(0,256))

print('Added ' + str(main) + ' to ' + str(deloc) + ' which gives us ' + str(int(main) + int(deloc)))