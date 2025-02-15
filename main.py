# IMPORT FUNCTIONs
from doBackup import makeBackup
from file import replaceNameFileBackup
from sendEmail import sendEmail
from time import sleep
from datetime import datetime
import schedule


def initBackup():
    # FAZENDO O BACKUP DO SISTEMA
    makeBackup()

    # PEGANDO O NOME DO ARQUIVO DO BACKUP
    file = replaceNameFileBackup()

    # ENVIANDO O EMAIL COM ANEXO DO ARQUIVO DE BACKUP
    sendEmail(file)

# AGENDAMENTO PARA INICIALIZAÇÃO DO BACKUP AS 9H DA MANHA E AS 10 PRAS 6H DA NOITE
schedule.every().day.at("09:00").do(initBackup)
schedule.every().day.at("17:52").do(initBackup)

while True:
    schedule.run_pending()
    sleep(60)
  