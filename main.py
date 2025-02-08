# IMPORT FUNCTIONs
from doBackup import makeBackup
from file import replaceNameFileBackup
from sendEmail import sendEmail
from time import sleep
from datetime import datetime
import schedule

# FUNÇÃO QUE VERIFICA A HORA DO DIA E DETERMINA SE SERÁ FEITO O BACKUP OU NÃO
def makeBackOrNotMake():
    # RECEBENDO A HORA ATUAL
    date = datetime.now()

    # CONVERTENDO EM STRING
    date= str(date)

    # DIVIDINDO A DATA DA HORA
    date = date.split(" ")

    # PEGANDO A HORA COMPLETA E RETIRANDO APENAS O VALOR DA HORA
    date = date[1].split(':')

    # CONVERTENDO O VALOR DA HORA EM INTEIRO
    hora = int(date[0])

    # VERIFICANDO SE A HORA ATUAL É MAIOR QUE 9
    if hora > 16:
        makeBackup()


# FUNÇÃO QUE COPIA O ARQUIVO DE BACKUP PARA A RAIZ DA APLICAÇÃO
def copyFileBackup():
    makeBackOrNotMake()
    return replaceNameFileBackup()

# FUNÇÃO QUE DISPARA O ENVIO DO EMAIL
def sendEmailBackup():
    file = copyFileBackup()
    sendEmail(file)


schedule.every().day.at("09:00").do(sendEmailBackup)
schedule.every().day.at("17:50").do(sendEmailBackup)

while True:
    schedule.run_pending()
    sleep(60)
  