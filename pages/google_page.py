from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from browser import Browser
from utils.reporte_util import ReporteUtil


# Instanciando Reporte para poder adicionar passos no report
report = ReporteUtil()


# Seletores dos elementos utilizados na página
class GooglePageLocator(object):
    INPUT_PESQUISA = '[name="ffq"]'
    BUTTON_PESQUISAR = '.FPdoLc [name="btnK"]'
    TITLE_RESULTADO = '[data-attrid="title"]'


class GooglePage(Browser):

    # TODO: Colocar em uma classe generica
    def get_element(self, locator):
        try:
            # Aguarda elemento estar visível na tela
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return self.driver.find_element(By.CSS_SELECTOR, locator)

        except Exception as erro:
            report.log_print_fail(f'Erro ao capturar elemento com locator "{locator}"! - ERRO: {str(erro)}')
            raise

    def acessar_pagina(self, url):
        try:
            self.driver.get(url)
            report.log_print_pass('Acessou ' + url)

        except Exception as erro:
            report.log_print_fail(f'Erro ao acessar url "{url}"! - ERRO: {str(erro)}')
            raise

    # TODO: Colocar em uma classe generica
    def preenche_campo_pesquisa(self, texto):
        try:
            input_pesquisa = self.get_element(GooglePageLocator.INPUT_PESQUISA)
            input_pesquisa.send_keys(texto)
            input_pesquisa.send_keys(Keys.TAB)

            report.log_print_pass(f'Preencheu campo com texto: "{texto}"')

        except Exception as erro:
            report.log_print_fail(f'Erro ao prencher campo! - ERRO: {str(erro)}')
            raise

    def clica_botao_pesquisar(self):
        try:
            button = self.get_element(GooglePageLocator.BUTTON_PESQUISAR)
            report.log_print_pass('Clicou no botao pesquisar', False)
            button.click()

        except Exception as erro:
            report.log_print_fail(f'Erro ao clicar no botão pesquisar! - ERRO: {str(erro)}')
            raise

    def get_texto_resultado(self):
        try:
            element = self.get_element(GooglePageLocator.TITLE_RESULTADO)
            report.log_print_pass('Retornou texto ' + element.text)
            return element.text

        except Exception as erro:
            report.log_print_fail(f'Erro ao capturar texto do resultado! - ERRO: {str(erro)}')
            raise
