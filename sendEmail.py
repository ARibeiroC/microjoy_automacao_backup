import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def sendEmail(fileName):
    print("Iniciando o envio do email")
    subject = "Backup Ouro Moderno"
    body = f"backup do banco de dados da Ouro Modernos"
    sender_email = "devribeiroanderson@gmail.com"
    recipients_email = ["devribeiroanderson@gmail.com"]
    sender_password = "xtuo cdmk qnkr ecis"
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    path_to_file = fileName

    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = ', '.join(recipients_email)
    body_part = MIMEText(body)
    message.attach(body_part)

    # Adicionando o anexo
    with open(path_to_file,'rb') as file:
        # colocando no anexo no email
        message.attach(MIMEApplication(file.read(), Name=fileName))

    # secction 2 for sending email
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipients_email, message.as_string())

    print("Email Enviado com sucesso!")


if __name__ == "__main__":
    sendEmail("backup-11-01-2025_10-02-32.zip")


