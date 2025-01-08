import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.udemy.com/join/passwordless-auth/?next=%2Fcourse%2Fthe-complete-web-development-bootcamp%2Flearn%2Flecture%2F12286990%3Fstart%3D30#overview")
time.sleep(3)


navegador.find_element('xpath', '//*[@id="form-group--1"]').click()
navegador.find_element('xpath', '//*[@id="form-group--1"]').send_keys("mateus.16.veloso@gmail.com")

time.sleep(3)
