from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M")

navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys("Mateus Veloso")

navegador.find_element('xpath',
                        '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys("mateus123@gmail.com")

navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys("031983108147")

navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button').click()

input("Press Enter to close the browser..")

