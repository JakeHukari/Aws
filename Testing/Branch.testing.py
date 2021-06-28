import random
import os

os.system('cls')

main = int(input("Enter a number: "))
deloc = int(random.randint(0,255))

print('Added ' + str(main) + ' to ' + str(deloc) + ' which gives us ' + str(int(main) + int(deloc)))