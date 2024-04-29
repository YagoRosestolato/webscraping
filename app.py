from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://lp.hashtagtreinamentos.com/esperapythonimpressionador?origemurl=hashtag_yt_org_listaesperapython_8AMNaVt0z_M")
navegador.find_element('xpath', '//*[@id="botaoPopup1"]').click()
navegador.find_element('xpath', '//*[@id="firstname"]').send_keys('Yago')
navegador.find_element('xpath', '//*[@id="email"]').send_keys('yagorosestolato@hotmail.com')
navegador.find_element('xpath', '//*[@id="phone"]').send_keys('24981239093')
navegador.find_element('xpath', '//*[@id="_form_2475_submit"]').click()

navegador.find_element('xpath', '/html/body/div[1]/div[2]/div/div/div[1]/div/span[2]').get_text().strip()


print(navegador)