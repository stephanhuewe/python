import random
from datetime import date

rowToCheck = random.randint(1, 7)
todayDate = date.today()
print ("=================================================================")
print ("=========================3G Check================================")
print (f"Geprüft wird heute ({todayDate}) die Reihe: {rowToCheck}")
print ("=================================================================")
