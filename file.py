import shutil
import os
from datetime import datetime

def fileNameToday():
    today = datetime.now()
    # TRATANDO O NOME DO ARQUIVO
    today = str(today.strftime("%d-%m-%Y"))
    nameFile = f'backup-{today}'

    # RETORNANDO O NOME DO ARQUIVO COM A DATA E HORARIO ATUAL
    return nameFile

def copyFile(fileBackup):
    # Caminho do arquivo original
    origem = f"C:/wamp/www/_bkp/{fileBackup}"

    # Novo destino do arquivo
    destino = "C:/Users/ander/Documents/system-backup-microjoy"

    # Movendo o arquivo
    shutil.copy(origem, destino)
    print("Arquivo movido com sucesso!")


def replaceNameFileBackup():
    # PEGANDO O NOME DO ARQUIVO DE BACKUP
    nameFile = fileNameToday()

    # SETANDO O CAMINHO DA PASTA ONDE ESTA O ARQUIVO DE BACKUP DO SISTEMA
    path = "C:/wamp/www/_bkp"

    # ARMAZENANDO OS NOMES DE TODOS OS ARQUIVOS DA PASTA EM UMA LISTA
    files = os.listdir(path)

    # VERIFICANDO SE O NOME DO ARQUIVO DE BACKUP ESTA NA LISTA DE ARQUIVOS DA PASTA DE BACKUP DO SISTEMA
    for file in files:

        # ARMAZENANDO O NOME DO ARQUIVO DE BACKUP DO DIA NA VARIÁVEL
        if file.find(nameFile) == 0:
            nameFileBackup = file

    # COPIANDO O ARQUIVO PARA A PASTA RAIZ
    copyFile(nameFileBackup)

    # RETORNA O NOME DO ARQUIVO DO BACKUP
    return nameFileBackup



if __name__ == "__main__":
    replaceNameFileBackup()
