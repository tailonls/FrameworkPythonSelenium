from pyhtmlreport import Report
from browser import Browser
import os

browser = Browser()
ROOT_DIR = os.path.dirname('target/report/')


class Reporte_util(object):
    report = Report()

    def inicializa_report(self):
        self.report.setup(
            report_folder=ROOT_DIR,
            module_name='Tsstes no Google',
            release_name='Release Default',
            selenium_driver=browser.get_driver()
        )

    def add_test_in_report(self, titulo_cenario, numero_teste):
        self.report.write_step(
            titulo_cenario,
            status=self.report.status.Start,
            test_number=numero_teste
        )

    def log_print_pass(self, texto):
        self.report.write_step(
            texto,
            status=self.report.status.Pass,
            screenshot=True
        )

    def log_print_fail(self, texto):
        self.report.write_step(
            texto,
            status=self.report.status.Fail,
            screenshot=True
        )

    def finaliza_report(self):
        self.report.generate_report()
