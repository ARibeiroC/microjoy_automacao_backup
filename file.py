import shutil
import os
from datetime import datetime

def fileNameToday():
    today = datetime.now()
    # TRATANDO O NOME DO ARQUIVO
    today = str(today.strftime("%d-%m-%Y"))
    nameFile = f'backup-{today}'
    return nameFile

def copyFile(fileBackup):
    # Caminho do arquivo original
    origem = f"C:/wamp/www/_bkp/{fileBackup}"

    # Novo destino do arquivo
    destino = "C:/Users/ander/Documents/sistem-backup"

    # Movendo o arquivo
    shutil.copy(origem, destino)
    print("Arquivo movido com sucesso!")


def replaceNameFileBackup():
    nameFile = fileNameToday()
    path = "C:/wamp/www/_bkp"
    files = os.listdir(path)
    for file in files:
        if file.find(nameFile) == 0:
            nameFileBackup = file

    copyFile(nameFileBackup)
    return nameFileBackup



if __name__ == "__main__":
    replaceNameFileBackup()
