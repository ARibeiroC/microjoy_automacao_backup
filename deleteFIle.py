import os
from datetime import date

path =  path = "C:/Users/ander/Documents/sistem-backup"

def deleteFile(file):
    pass

day, day2 = ''
month, month2 = ''
year, year2 = ''
def findOldFile():
    files = os.listdir(path)
    bkps = []
    for file in files:
        if 'backup' in file:
            bkps.append(file)
        
    for bkp in bkps:
        today = date.today()
        
        name = bkp.split('_')
        name.pop(1)
        name = name[0].split('-')
        del name[0]

    print(day, month, year)
    # os.remove(bkps[0])


findOldFile()