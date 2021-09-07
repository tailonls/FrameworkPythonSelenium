import os

from pyhtmlreport import Report

from browser import Browser

browser = Browser()
ROOT_DIR = os.path.dirname('target/report/')


class ReporteUtil(object):
    report = Report()

    def inicializa_report(self):
        # Verificando se diretório existe
        if not os.path.isdir(ROOT_DIR):
            os.makedirs(ROOT_DIR)

        self.report.setup(
            report_folder=ROOT_DIR,
            module_name='Testes no Google',
            release_name='Release Default',
            selenium_driver=browser.get_driver()
        )

    def add_test_in_report(self, titulo_cenario, numero_teste):
        self.report.write_step(
            titulo_cenario,
            status=self.report.status.Start,
            test_number=numero_teste
        )

    def log_print_pass(self, texto, screenshot=True):
        self.report.write_step(
            texto,
            status=self.report.status.Pass,
            screenshot=screenshot
        )

    def log_print_fail(self, texto, screenshot=True):
        self.report.write_step(
            texto,
            status=self.report.status.Fail,
            screenshot=screenshot
        )

    def finaliza_report(self):
        self.report.generate_report()
