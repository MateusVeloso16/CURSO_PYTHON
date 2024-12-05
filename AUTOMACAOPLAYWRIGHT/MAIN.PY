from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://www.hashtagtreinamentos.com/curso-python")
#    pagina.locator('xpath=/html/body/main/section[1]/div/div[1]/form/div/div[1]/input').click()
    pagina.fill('xpath=/html/body/main/section[1]/div/div[1]/form/div/div[1]/input', "Mateus")
#    pagina.locator('xpath=/html/body/main/section[1]/div/div[1]/form/div/div[2]/input').click()
    pagina.fill('xpath=/html/body/main/section[1]/div/div[1]/form/div/div[2]/input', "mateus123@gmail.com")
#    pagina.locator('xpath=/html/body/main/section[1]/div/div[1]/form/div/div[3]/input').click()
    pagina.fill('xpath=/html/body/main/section[1]/div/div[1]/form/div/div[3]/input', "31983108147")
    pagina.locator('xpath=/html/body/main/section[1]/div/div[1]/form/button').click()
    time.sleep(10)
