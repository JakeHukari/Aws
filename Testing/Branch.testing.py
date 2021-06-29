import random
import os

os.system('cls')

print('log test')

main = int(input("Enter a number: "))
deloc = int(random.randint(0,256))

print('Added ' + str(main) + ' to ' + str(deloc) + ' which gives us ' + str(int(main) + int(deloc)))