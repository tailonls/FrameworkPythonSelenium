from selenium import webdriver


class Browser(object):
    # Inicia o browser chrome, mas pode ser feito com outros como Firefox, Safari e IE
    driver = webdriver.Chrome('C:/bin/chromedriver.exe')

    # Define o tempo maximo para carregamento da pagina
    driver.set_page_load_timeout(30)

    # Maximiza a janela do browser ao ser iniciado
    driver.maximize_window()

    # Retorna instancia do driver
    def get_driver(self):
        return self.driver

    # Fecha o browser
    def browser_quit(self):
        self.driver.quit()

    # Limpa o browser
    def browser_clear(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script('window.localStorage.clear()')
        self.driver.execute_script('window.sessionStorage.clear()')
        self.driver.refresh()
