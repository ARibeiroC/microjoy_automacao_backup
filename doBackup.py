from driver import driver, By
from time import sleep

def makeBackup():
    print("Iniciando o bakcup")
    driver.maximize_window()
    driver.get("http://localhost")


    user = driver.find_element(By.NAME, value="aluno")
    password = driver.find_element(By.NAME, value='senha')
    submit_button = driver.find_element(By.CLASS_NAME, value="btn-login")
    user.send_keys('Admin')
    sleep(2)
    password.send_keys('Master')
    sleep(2)
    submit_button.click()
    sleep(10)
    menuManutencao = driver.find_element(By.ID, value="menuManutencao")
    menuManutencao.click()
    sleep(3)
    backup = driver.find_element(By.CLASS_NAME, value="fa-cloud-download")
    backup.click()
    sleep(5)
    doBackup = driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/ul/li[1]/a')
    doBackup.click()
    sleep(5)
    driver.close()
    print('backup concluído')

if __name__ == "__main__":
    makeBackup()