# Automação de Backup
Automação desenvolvida para fazer backup do banco de dados MySQL com WAMP Server, através da aplicação web da Ouro Moderno, após a realização do backup, ele faz uma cópia do arquivo para a raiz da automação e depois dispara um e-mail para os diretores da escola.

## DESCRIÇÃO
Para poder realizar essa automação foi preciso importar a bibliotecas (Selenium), onde o Selenium foi responsável para acessar a interface da aplicação web e iniciar o backup, depois foi utilizado outras 3 Libs (Shutil, OS, Datetime) para fazer a cópia do arquivo para a pasta raiz do projeto, para disparar o e-mail utilizei as libs (smtpLib, MIMEText, MIMEMultipart e MIMEApplication), e por fim, para integrar a automação ao sistema operacional e adiciona-lo ao agendamento de tarefas do windows, foi utilizado a lib (PyInstaller) para compilar e gerar um arquivo executável, a partir disso, abri o agendador de tarefas do windows e adicionei o APP na rotinas de execução do sistema operacional.
