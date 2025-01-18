# IMPORT FUNCTIONs
from doBackup import makeBackup
from file import replaceNameFileBackup
from sendEmail import sendEmail
from time import sleep
import schedule

def initializeBackup():
    makeBackup()


def copyFileBackup():
    return replaceNameFileBackup()

def sendEmailBackup():
    file = copyFileBackup() 
    sendEmail(file)

schedule.every().day.at("17:52").do(initializeBackup)

schedule.every().day.at('17:54').do(sendEmailBackup)

while True:
    schedule.run_pending()
    sleep(1)

    